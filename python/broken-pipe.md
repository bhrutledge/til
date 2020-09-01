# Avoid broken pipe errors from Python scripts

For example:

```
$ python my_script.py | head
...
BrokenPipeError: [Errno 32] Broken pipe
```

Combining the Python docs' [Note on SIGPIPE](https://docs.python.org/3/library/signal.html#note-on-sigpipe) with a [context manager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager):

```python
import os
import sys
from contextlib import contextmanager


@contextmanager
def pipeable():
    """
    Silence noisy errors from `python my_script.py | head`.

    https://docs.python.org/3/library/signal.html#note-on-sigpipe
    """
    try:
        yield
    except BrokenPipeError:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(1)


def main():
    data = get_data()
    with pipeable():
        sys.stdout.write(data)

# ...

if __name__ == "__main__":
    main()
```

It can also be used as a decorator:

```python
@pipeable()
def main():
    data = get_data()
    sys.stdout.write(data)
```

**Don't** use [this workaround](https://stackoverflow.com/a/16865106/3188289) (per the "Note" linked above):

```python
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
```
