# History
## Some Settings

- export HISTSIZE=1000
- export HISTFILESIZE=2000
- export HISTCONTROL=ignoredups: ignore duplicate
- export HISTIGNORE=”&:ls:[bf]g:exit:history”
- export HISTTIMEFORMAT=’%F %T ‘
    - %F: Year-Month-Day
    - %T: Time in 24h format
    - More info: man strftime

## Clear history in bash:

- history -c: clear all history
- history -d <entry>: delete specific entry

## Clear history in zsh:

- As history -c and -d doesn’t work in zsh, edit ~/.zsh_history and kill current shell without saving history
```bash
echo > .zsh_history && kill -9 $$
```

## Call history command:

- !<cmd number>: run command with number
- !!: run last command
- !<part of command>: search backward for command that has that part, press <TAB> to complete command or just enter to run first command found
- !<keyword>:p: to print, not run
- Ctrl_R: Search for command
- <new command> !$: reuse previous last argument of old command with <new command>
- <new command> !^: reuse previous first argument of old command with <new command>
- <new command> !*: reuse all previous arguments of old command with <new command>
- <new command> !<searched cmd>:<argument number>: search for <searched cmd>, reuse its argument number (start from 0) and run with <new command>
- ^<text to search from previous command>^<text to replace>: replace/modify text from last command, then run

## Reference

- https://www.howtogeek.com/howto/44997/how-to-use-bash-history-to-improve-your-command-line-productivity/