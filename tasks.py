"""
Based on:
https://github.com/simonw/til/blob/06061ab94ddbb37afd0277454c5bd08bb4b5df13/build_database.py
https://github.com/simonw/til/blob/06061ab94ddbb37afd0277454c5bd08bb4b5df13/update_readme.py
"""
import pathlib
import re
from datetime import timezone

import git
import sqlite_utils
from invoke import task

root = pathlib.Path(__file__).parent.resolve()
db_path = root / "til.db"

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)
count_re = re.compile(r"<!\-\- count starts \-\->.*<!\-\- count ends \-\->", re.DOTALL)

COUNT_TEMPLATE = "<!-- count starts -->{}<!-- count ends -->"


def created_changed_times(repo_path, ref="main"):
    created_changed_times = {}
    repo = git.Repo(repo_path, odbt=git.GitDB)
    commits = reversed(list(repo.iter_commits(ref)))
    for commit in commits:
        dt = commit.committed_datetime
        affected_files = list(commit.stats.files.keys())
        for filepath in affected_files:
            if filepath not in created_changed_times:
                created_changed_times[filepath] = {
                    "created": dt.isoformat(),
                    "created_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            created_changed_times[filepath].update(
                {
                    "updated": dt.isoformat(),
                    "updated_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            )
    return created_changed_times


@task
def build_database(c):
    db_path.unlink(missing_ok=True)
    db = sqlite_utils.Database(db_path)
    table = db.table("til", pk="path")

    all_times = created_changed_times(root)

    for filepath in root.glob("*/*.md"):
        fp = filepath.open()
        title = fp.readline().lstrip("#").strip()
        body = fp.read().strip()
        path = str(filepath.relative_to(root))
        record = {
            "path": path,
            "topic": path.split("/")[0],
            "title": title,
            "body": body,
        }
        record.update(all_times[path])
        table.insert(record)

    if "til_fts" not in db.table_names():
        table.enable_fts(["title", "body"])


@task(build_database)
def update_readme(c, rewrite=False):
    db = sqlite_utils.Database(db_path)

    by_topic = {}
    for row in db["til"].rows_where(order_by="created_utc"):
        by_topic.setdefault(row["topic"], []).append(row)

    index = ["<!-- index starts -->"]
    for topic, rows in by_topic.items():
        index.append("## {}\n".format(topic))
        for row in rows:
            index.append(
                "* [{title}]({path}) - {date}".format(
                    date=row["created"].split("T")[0], **row
                )
            )
        index.append("")
    if index[-1] == "":
        index.pop()
    index.append("<!-- index ends -->")

    if rewrite:
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        rewritten = index_re.sub(index_txt, readme_contents)
        rewritten = count_re.sub(COUNT_TEMPLATE.format(db["til"].count), rewritten)
        readme.open("w").write(rewritten)
    else:
        print("\n".join(index))
