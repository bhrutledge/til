# Uninstall all Python packages with pip

```bash
python -m pip freeze | xargs python -m pip uninstall -y
```

Or, using [process substitution](https://www.tldp.org/LDP/abs/html/process-sub.html):

```bash
python -m pip uninstall -y -r <(python -m pip freeze)
```

This is more convenient than deleting and re-creating a virtual environment. It's also handy for cleaning up your "system" Python environment.

From [Stack Overflow](https://stackoverflow.com/a/11250821/3188289).
