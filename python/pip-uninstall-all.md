# Uninstall all Python packages with pip

Via [Stack Overflow](https://stackoverflow.com/a/11250821/3188289):

```bash
pip freeze | xargs pip uninstall -y
```

This is more convenient than deleting and re-creating a virtual environment.
