# Writing CSV files without CRLF

```python
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator="\n")
writer.writeheader()
writer.writerows(rows)
```

Without `lineterminator`, lines will end with `\r\n`, which can result in:

```
$ git add .
fatal: CRLF would be replaced by LF in test.csv
```

It might be preferable to use `os.linesep`, instead of `"\n"`, but I don't know if that's the correct behavior on Windows.

Sources (including other workarounds):

- [CSV in Python adding an extra carriage return, on Windows - Stack Overflow](https://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return-on-windows)
- [How to write CSV output to stdout? - Stack Overflow](https://stackoverflow.com/questions/23665264/how-to-write-csv-output-to-stdout)
- [`csv.writer` — Python 3 documentation](https://docs.python.org/3/library/csv.html#csv.writer)
