# Hashcat installation on MacOS
## Commands

- brew install hashcat

## Permission Issues
```bash
brew install hashcat     
Error: The following directories are not writable by your user:
/usr/local/lib/pkgconfig
/usr/local/share/man/man1
/usr/local/share/zsh
/usr/local/share/zsh/site-functions

You should change the ownership of these directories to your user.
  sudo chown -R $(whoami) /usr/local/lib/pkgconfig /usr/local/share/man/man1 /usr/local/share/zsh /usr/local/share/zsh/site-functions

And make sure that your user has write permission.
  chmod u+w /usr/local/lib/pkgconfig /usr/local/share/man/man1 /usr/local/share/zsh /usr/local/share/zsh/site-functions

And running brew with sudo is not allowed

sudo brew install hashcat
Error: Running Homebrew as root is extremely dangerous and no longer supported.
As Homebrew does not drop privileges on installation you would be giving all
build scripts full access to your system.
```

## Change Owner on related files
- sudo chown -R <user>:admin /usr/local/*