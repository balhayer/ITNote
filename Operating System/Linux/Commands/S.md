# SED (Stream Editor)
## Change hostname

- sudo sed -i ‘s/.*/<new name>/’ /etc/hostname

## Prepend text to a file

- sed -I ‘1s/^/<text to prepend>\n/’ <file>
```Bash
# cat testfile
line 1
line 2
line 1
line 3
# sed -i '1s/^/line 0\n/' testfile
# cat testfile
line 0
line 1
line 2
line 1
line 3
# vi testfile
# sed -i '2s/^/line -1\n/' testfile
# cat testfile
line 0
line -1
line 1
line 2
line 3
line 4
# sed -i '3s/^/line -2\n/' testfile
# cat testfile
line 0
line -1
line -2
line 1
line 2
line 3
line 4
```

## Insert a line in the middle

- sed -i ‘2 i whatever text to add’ file.txt

## Delete a line

- sed -i ‘2 d’ file.txt

## Combine multiple lines to one line

- cat text | tr ‘\n’ ‘ ‘ | sed ‘s/ //g’
    - Tr ‘\n’ ‘<space>’: change new line to space
    - Then sed ‘s/<space>//g’: change all <space> to none

## Print /Start/ /End/

- ansible-doc ios_facts | sed -n ‘/^# hardware/,/^$/p’: print section from # hardware to blank line
    - -n: quiet mode
## Reference
- https://www.cyberciti.biz/faq/bash-prepend-text-lines-to-file/

===========================================================================================================
# Shift - Shift positional parameters
```bash
cat test.sh
#!/bin/bash

echo $1
echo $2
echo $3
shift 2
echo $@

./test.sh one two three four
one
two
three
three four
```
===========================================================================================================
# Sudo and Visudo

## Edit sudo configuration

- sudo visudo
- Order is important, the last config is applied

### Sample configuration
```bash
# Cmnd alias specification
Cmnd_Alias CMD_SHUTDOWN=/usr/sbin/shutdown 1,/usr/sbin/shutdown 5

# Allow members of group sudo to execute any command                                    │
%sudo   ALL=(ALL:ALL) ALL

# User privilege specification
root    ALL=(ALL:ALL) ALL
kali    ALL=(root:root) NOPASSWD:/usr/bin/nmap
kali    ALL=(root:root) NOPASSWD:CMD_SHUTDOWN

#User  Host=(runas user:runas group) Command
```

## Commands

- sudo -k: Clear sudo cache