## Initialize Repository

git init
git config user.mail <email address>
git config user.name <Name>

## Setting name and email globally
    git config --global user.name "Your Name"
    git config --global user.email you@example.com

### After doing this, you may fix the identity used for this commit with:
    git commit --amend --reset-author

## Check status, add files and Commit
```bash
git add .
git commit -m "<comment>"
git status
git remote -v
```
## Add Remote Repository
```bash
git remote add origin <url to remote repository>
git push -u origin master
```

### If remote branch is main
```bash
git remote add origin <url to remote repository>
git branch -M main
git push -u origin main
```

## Update Remote Repository/Change from HTTPS to SSH and vice versa
```bash
git remote set-url origin <new URL>: fetch
git remote set-url --push origin <new URL>: push
```

## Git Credential
```bash
Git config --global credential.helper store: store credential in file on disk
Git config credential.helper cache <timeout>: cache credential for 900s = 15 mins by default
Git config credential.helper wincred|osxkeychain: use the native format of their backing stores
```

## Remove Outdated branch (deleted remotely) from local database
```bash
git fetch --prune
Command Pallete (Ctrl-Shift-P or F1): git:fetch(Prune) Visual Studio Code
```

## Remove settings
```bash
git config --global --unset user.email
git config --global --unset user.name
Git config --global --unset credential.helper: remove credential
```

## Remove files from previous commit which was commited

### Use git show to find which commit has that file
```bash
- git reset HEAD:file.txt
- git reset HEAD~1:file.txt   
```

### After finding which commit has file.txt, reset to 1 commit before that so that it doens't have that file:
- git reset HEAD~2

### Add all current file to git and commit, then push to github as usual
- git add .
- git commit -m "Some message"

## Using 2 Git accounts

### SSH Configuration
```bash
#Account1
Host github.com
HostName github.com
User git
AddKeysToAgent yes
UseKeychain yes
IdentityFile ~/key1

#Account2
Host github.com-2
HostName github.com
User git
AddKeysToAgent yes
UseKeychain yes
IdentityFile ~/key2
When adding remote for Account2, use the following url
git@github.com-2:username/repo.git
```

### When pushing repository to github, may need to remove cached ssh-key so git can use the right key for authentication
```bash
ssh-add -l: list all identities
ssh-add -D: delete all identities
git push: to push to github, the right key will be used for corresponding account
```

## Reference

- A successful git branching model: nvie.com/posts/a-successful-git-branching-model/
- https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage
- https://www.heady.io/blog/how-to-manage-multiple-github-accounts
