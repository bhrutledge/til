# Use `python -c` one-liners to supplement shell commands

I found myself wanting to [percent encode](https://en.wikipedia.org/wiki/Percent-encoding) a string on the command line (and eventually a [shell script](https://github.com/bhrutledge/dotfiles/blob/master/src/.local/bin/gh-search-repos)). I wasn't able to find a simple Bash one-liner, but it is [built into Python](https://docs.python.org/3.3/library/urllib.parse.html?highlight=urlencode#url-quoting). Using the `-c` option with trivial command-line parsing yields:

```
$ python -c 'import sys, urllib.parse; print(urllib.parse.quote_plus(sys.argv[1]))' 'foo bar'
foo+bar
```

Or, to process multiple lines (e.g., via a [here document](https://en.wikipedia.org/wiki/Here_document)) as a single string:

```
$ python -c 'import sys, urllib.parse; print(urllib.parse.quote_plus(sys.stdin.read().strip()))' <<EOF
> foo bar
> one, two, three
> EOF
foo+bar%0Aone%2C+two%2C+three
```

To process each line, you might try a `for` loop, but that doesn't work with the `import`:

```
$ python -c 'import sys, urllib.parse; for l in sys.stdin: print(urllib.parse.quote_plus(l.strip()))' < lines.txt
  File "<string>", line 1
    import sys, urllib.parse; for l in sys.stdin: print(urllib.parse.quote_plus(l.strip()))
                              ^
SyntaxError: invalid syntax
```

One workaround is to type a literal newline:

```
$ python -c '
> import sys, urllib.parse
> for l in sys.stdin: print(urllib.parse.quote_plus(l.strip()))' < lines.txt
foo+bar
one%2C+two%2C+three
```

Or, use [ANSI-C quoting](https://www.gnu.org/software/bash/manual/html_node/ANSI_002dC-Quoting.html#ANSI_002dC-Quoting) to allow the newline character:

```
$ python -c $'import sys, urllib.parse\nfor l in sys.stdin: print(urllib.parse.quote_plus(l.strip()))' < lines.txt
foo+bar
one%2C+two%2C+three
```

Sources:

- [How can I encode and decode percent-encoded strings on the command line? - Ask Ubuntu](https://askubuntu.com/a/1110641)
- [Passing line-feed(LF)/new-line character as an argument in bash - Stack Overflow](https://stackoverflow.com/a/46886035/3188289)
- [The surprisingly difficult task of printing newlines in a terminal | victoria.dev](https://victoria.dev/blog/the-surprisingly-difficult-task-of-printing-newlines-in-a-terminal/)
