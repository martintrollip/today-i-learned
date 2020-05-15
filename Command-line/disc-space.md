- Date : 2020-05-14
- Tags : #Command-line

## Disc space


You can check the disc space by using one of the following


### Disc Space

```
df -h      
du -m -h --max-depth 1 | sort -rn (all folders in dir)
```

### Size of dir

```
du -ch | grep total
```


`-h` means the results will be printed in a human-readable format

