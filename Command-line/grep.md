- Date : 2020-05-15
- Tags : #Command-line

## grep

**Stands for** Global regular expression print
**Funtion** Search for PATTERN in each FILE or standard input

grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p, which has the same effect. grep was originally developed for the Unix operating system, but later available for all Unix-like systems and some others such as OS-9

### Search for string in a file example

```
grep -C 10 "string I'm looking for" stdout.log
```

[Wikipedia](https://en.wikipedia.org/wiki/Grep)
