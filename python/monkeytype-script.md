# Add type annotations to a Python script with MonkeyType

Given a `script.py` like:

```python
def main():
    for line in get_lines(5):
        print(line)


def get_lines(count):
    return [f"Line {x + 1}" for x in range(count)]


if __name__ == "__main__":
    main()
```

Use a temporary runner script to trace the script:

```
$ echo 'import script; script.main()' > run_script.py

$ monkeytype run run_script.py
Line 1
Line 2
Line 3
Line 4
Line 5
```

Apply the annotations and clean up:

```
$ monkeytype apply script

$ rm -f run_script.py monkeytype.sqlite3
```

Result:

```python
from typing import List

def main() -> None:
    for line in get_lines(5):
        print(line)


def get_lines(count: int) -> List[str]:
    return [f"Line {x + 1}" for x in range(count)]


if __name__ == "__main__":
    main()
```

Source:

- [monketype fails to stub the initial script · Issue #19 · Instagram/MonkeyType](https://github.com/Instagram/MonkeyType/issues/19)
- [Tracing function calls — MonkeyType documentation](https://monkeytype.readthedocs.io/en/latest/tracing.html#monkeytype-run)
