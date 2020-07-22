- Date : 2020-07-22
- Tags : #Git

## Copy file preserving history

In Git it is tricky to copy a file and preserve it's history since Git does not keep track of which files chaged.  The commit data structure points to previous commits without explicit information about which files are changed in a commit. 

Git diff tools can use heuristics to determine if a file was renamed for example, but usually it's seen as one file being deleted and another being created. 

There is a way to copy a file and preserving the history though; 

1. Move the file to 2 different locations
2. Merge the two commits that do 1. 
3. Move one copy back to the original location

[StackOverflow answer and nice explaination](https://stackoverflow.com/a/44036771/1859777)

[StackOverflow answer with a script)[https://stackoverflow.com/a/53849613/1859777]

