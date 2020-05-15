- Date : 2020-05-13
- Tags : #Git

## Soft reset

Reset the HEAD to another commit

```
git reset --soft HEAD~  (n-1 commits)
git reset --soft HEAD~2
git reset --soft HEAD~10
```

To undo commits which wasn't pushed yet.  The index and working directories remains unchanged and changed files are staged. 


[git reset soft When to Use Git, Reset, Git Revert and Git checkout](https://dev.to/neshaz/when-to-use-git-reset-git-revert--git-checkout-18je)
