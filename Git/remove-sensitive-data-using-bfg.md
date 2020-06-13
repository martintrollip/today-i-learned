- Date : 2020-06-13
- Tags : #Git

## Remove sensitive data using BFG

Say for example you commited a password, API key, or any sensitive information in a repository.  Simply reverting the commit or manually removing the password won't work because it is still part of the Git history.  A rebase might work if you're not too far ahead.   

The BFG is really handy in this regard. It's an open source repo cleaner written in Scala. The BFG is a simpler, faster alternative to `git-filter-branch` for cleansing bad data out of your Git repository history.

Steps: 

1. Clone your repo using `--mirror`  `$ git clone --mirror git://example.com/some-big-repo.git`
2. Create a file `passwords.txt` and include all of the passwords which has been committed. 
3. Run `$ bfg --replace-text passwords.txt some-big-repo.git`.  This will replace each of the passwords on the history with `**REMOVED**`. 
4. Read the output.  It will indicate if everything succeeded and if you need to do any manual deletions. 
5. `$ cd some-big-repo.git`
6. `$ git reflog expire --expire=now --all && git gc --prune=now --aggressive`
7. `$ git push`

[Removing sensitive data from a repository](https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository)

[BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

