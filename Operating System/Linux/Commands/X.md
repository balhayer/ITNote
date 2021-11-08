# Xclip - Copy content to x11 clipboard
## Installation

- apt-get install xclip

## Command

- Copy: xclip
- Paste: xclip -o

## Using with SSH session

- By default, use $DISPLAY environment variable. Can be set using -d option
- Refer to X11 Forwarding at https://hatinfosec.wordpress.com/2021/03/12/linux-ssh-command/

## Some Error

### Can’t copy data from SSH session to host machine clipboard (not remote machine’s clipboard)
- Reason: by default, xclip use primary selection
- Solution: use xclip -selection clipboard or xclip -sel c

### MacOS: Can copy data from SSH session (X11 Forwarding using xquartz) using xclip -sel c as in above case, but can’t paste it
- Reason: Pasteboard synching is not enabled
- Solution
    - Right Click at XQuartz -> Applications -> Customize
    - Then Under XQuartz menu -> Preferences (or Press Command ,)
    - Then Enable Synching
        - or Disable it, Close Preferences, then Reopen to enable it again.

# XXD
- xxd creates a hex dump of a given file or standard input
- It can also convert a hex dump back to its original binary form.

## Options

- -r: reverse
- -p: plain
- -ps: postscript

## Example

```bash
kali@kali:~$ echo test | xxd -p
746573740a
                                                                                                                                                                                  
kali@kali:~$ echo "746573740a" | xxd -r -p
test
```

## Reference
- https://www.tutorialspoint.com/unix_commands/xxd.htm
- https://manpages.ubuntu.com/manpages/trusty/man1/xxd.1.html