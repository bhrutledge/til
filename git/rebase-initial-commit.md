# Tidy up initial commits with `rebase --root`

When I first start a project, I often end up with bunch of small and "fixup" commits on the main branch. I think it's nice to keep a "clean" commit history. To squash those commits into the "initial" or "first" commit, use:

```
git rebase -i --root
```

I also used it for this repo, which started as a fork, but I didn't want the commit history from the parent repo. So, I used this command to drop all of the commits prior to mine.

Found via [Stack Overflow](https://stackoverflow.com/a/30277327/3188289). See also: [the docs](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---root).
