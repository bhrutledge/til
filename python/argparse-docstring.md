# Use a module's docstring in `argparse` help text

```python
"""
Process a file and print the results.

Long description and details of the processing.

  Example output
"""
import argparse


def main():
    description, epilog = __doc__.strip().split("\n\n")
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "file_path", help="Path of file to process", metavar="PATH"
    )
    args = parser.parse_args()


if __name__ == "__main__":
    main()
```

Result:

```
$ python process_file.py -h
usage: process_file.py [-h] PATH

Process a file and print the results.

positional arguments:
  PATH        Path of file to process

optional arguments:
  -h, --help  show this help message and exit

Long description and details of the processing.

  Example output
```

Via [Stack Overflow](https://stackoverflow.com/a/18107559/3188289) and [the Python docs](https://docs.python.org/3/library/argparse.html#formatter-class).
