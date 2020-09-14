# Format and lint Bash scripts

Use [shfmt](https://github.com/mvdan/sh#shfmt) for formatting, and [shellcheck](https://github.com/koalaman/shellcheck) for linting.

```
$ shfmt -i 4 -l -w script.sh

$ shellcheck script.sh
```

Both have editor extensions, e.g.:

- [shell-format - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=foxundermoon.shell-format)
- [shellcheck - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck)
