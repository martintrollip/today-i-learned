- Date : 2024-06-21
- Tags : #Git

## Enable OpenSSH Authentication Agent for Git

1. Enable the OpenSSH Authentication Agent service and make it start automatically.
2. Add your SSH key to the agent with `ssh-add` on the command line.
3. Test git integration, if it still asks for your passphrase, continue on.
4. Add the environment variable `$ENV:GIT_SSH=C:\Windows\System32\OpenSSH\ssh.exe` to your session, or permanently to your user environment.

[Why git can't remember my passphrase under Windows](https://stackoverflow.com/a/58784438/1859777)
