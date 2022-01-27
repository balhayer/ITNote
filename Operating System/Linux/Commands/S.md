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
- sed -si '/^$/d' file.txt: delete empty lines

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
# SSH

## Login using ID Key file
```bash
ssh -i <key file contains private key> user@server.com
```

Options:

- -oStrictHostKeyChecking=no: Doesn't check host key
- -c aes256-cbc: specify cipher to use
- -oHostKeyAlgorithms=+ssh-dss: specify host key algorithm to use
- -oKexAlgorithms=+diffie-hellman-group1-sha1: specify Host Key exchange algorithm to use
- Or use config file in ~/.ssh/config:
```bash
    Ciphers +aes128-ctr,aes192-ctr,aes256-ctr
    HostKeyAlgorithms ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-rsa,ssh-dss
    KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha256
    MACs hmac-sha2-256,hmac-sha2-512,hmac-sha1
```
 
- For some old devices:
```bash
    Ciphers +aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc
    HostKeyAlgorithms ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-rsa,ssh-dss
    KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha256,diffie-hellman-group1-sha1
    MACs hmac-sha2-256,hmac-sha2-512,hmac-sha1
```

## Port Forwarding

### Local Port Forwarding
```bash
- ssh -L 2000:<destination.to.access>:80 -N -f user@home.server

- From client (which initiate above ssh command), access port 2000, traffic will be forwarded to <destination to access> on port 80
-f ssh will go into background before executing the command
-N instruct ssh to not execute a command on remote system
```

### Remote Port Forwarding
```bash
ssh -R 2000:Corp.Server:22 user@external.server

- From external server or external client, access port 2000, traffic will be forwarded to <corp.server> on port 22
```

### Dynamic Forwarding
```bash
ssh -D <port> user@server.com

Connecting to <port> above using sock to forward all connection via server.com
```

## Add port forwarding to existing ssh session

- Linux ssh client:
    - <Enter>~C
    - -R 1234:localohost:4321
    - -L 8080:localhost:80
- Putty:
    - Right click on icon in the left top corner -> change setting
    - Go to ssh – Tunnel
- Reference:
    - https://coderwall.com/p/5wp2wg/start-port-forwarding-over-an-existing-ssh-connection-instead-of-creating-a-new-one
    - https://nixshell.wordpress.com/2008/12/10/ssh-port-forwarding-without-starting-a-new-session/
    - https://knowledge.exlibrisgroup.com/Voyager/Knowledge_Articles/Set_Up_SSH_Port_Forwarding_in_Putty

## Supported escape sequences:

- ~. – terminate connection (and any multiplexed sessions)
- ~B – send a BREAK to the remote system
- ~C – open a command line
- ~R – request rekey
- ~V/v – decrease/increase verbosity (LogLevel)
- ~^Z  – suspend ssh
- ~# – list forwarded connections
- ~& – background ssh (when waiting for connections to terminate)
- ~? – this message
- ~~ – send the escape character by typing it twice
- (Note that escapes are only recognized immediately after newline.)

## List background jobs and jump between ssh sessions:
```bash
server1#~^Z [suspend ssh]
 
[2]+  Stopped                 ssh user@10.10.10.1
admin@server:~/script$ jobs
[1]-  Stopped                 ssh user@10.10.10.2
[2]+  Stopped                 ssh user@10.10.10.1
admin@server:~/script$ fg 1
ssh user@10.10.10.2
 
server2#~^Z [suspend ssh]
 
[1]+  Stopped                 ssh user@10.10.10.2
admin@server:~/script$ jobs
[1]+  Stopped                 ssh user@10.10.10.2
[2]-  Stopped                 ssh user@10.10.10.1
admin@server:~/script$ fg 2
ssh user@10.10.10.1
```

## List forwarded connections/ports

- From remote shell of connected session, use command: ~#
- From terminal of client that connected to ssh server, use command: lsof -i -n | grep ‘ssh’

## Using config file
```bash
- File in ~/.ssh/config
- Permission: 600
- Example:
    Host server01
            Hostname 10.10.10.1
            User root
            IdentityFile ~/.ssh/idserver01
    Host server10
            Hostname 10.10.10.10
            User root
            IdentityFile ~/.ssh/idserver10
                ForwardAgent Yes
- Then can use command: ssh server01 to logon to 10.10.10.1
- Reference: https://linuxize.com/post/using-the-ssh-config-file/
```

## SSH-Agent and Agent Forwarding

- SSH using private key: ssh -i <key> <user>@<host>

### Adding Private Key to Memory:

- Run agent: eval ssh-agent -s or run ssh-agent to get SSH_AUTH_SOCK variable and prepend to ssh-add and ssh command
- Add Key: ssh-add <key file>.
- Key can be listed using: ssh-add -l
- If connecting to multiple boxes in a chain and they use different key, just add multiple key in this first agent
- Then can use that key in ssh without specifying key file, e.g. ssh user@host, Key will be used automatically from memory

### Example
```bash
Adding key to ssh agent: pageant is the ssh-agent of putty
        admin@server01:~/.ssh$ ssh-agent
        SSH_AUTH_SOCK=/tmp/ssh-y8F2O4AB8GfL/agent.25945; export SSH_AUTH_SOCK;
        SSH_AGENT_PID=25946; export SSH_AGENT_PID;
        echo Agent pid 25946;
        admin@server01:~/.ssh$ ssh-agent -s
        SSH_AUTH_SOCK=/tmp/ssh-68n3tMRvmmkQ/agent.25953; export SSH_AUTH_SOCK;
        SSH_AGENT_PID=25954; export SSH_AGENT_PID;
        echo Agent pid 25954;
        admin@server01:~/.ssh$ ssh-add hatinfosec
        Could not open a connection to your authentication agent. 
            ® This is because ssh-add doesn't know how to connect to ssh-agent. Reference: https://stackoverflow.com/questions/17846529/could-not-open-a-connection-to-your-authentication-agent
        admin@server01:~/.ssh$ eval `ssh-agent -s`
        Agent pid 25993
        admin@server01:~/.ssh$ ssh-add hatinfosec
        Identity added: hatinfosec (hatinfosec)
        admin@server01:~/.ssh$ ssh-add -l
        2048 SHA256:pdrSR6XzZu/t5QY/JPSHOebo/dqrJ1VMWo4JDD4Ww70 hatinfosec (RSA)
            ® This will only be available for this session only
```

### Another way to add key to agent:
```bash
admin@server01:~$ ssh-agent
SSH_AUTH_SOCK=/tmp/ssh-xlLGx8iT5DLr/agent.27033; export SSH_AUTH_SOCK;
SSH_AGENT_PID=27034; export SSH_AGENT_PID;
echo Agent pid 27034;

admin@server01:~$ ssh-add -l
Could not open a connection to your authentication agent.

admin@server01:~$ SSH_AUTH_SOCK=/tmp/ssh-xlLGx8iT5DLr/agent.27033 ssh-add -l
The agent has no identities.

admin@server01:~$ SSH_AUTH_SOCK=/tmp/ssh-xlLGx8iT5DLr/agent.27033 ssh-add .ssh/hatinfosec
Identity added: .ssh/hatinfosec (.ssh/hatinfosec)

admin@server01:~$ SSH_AUTH_SOCK=/tmp/ssh-xlLGx8iT5DLr/agent.27033 ssh-add -l
2048 SHA256:pdrSR6XzZu/t5QY/JPSHOebo/dqrJ1VMWo4JDD4Ww70 .ssh/hatinfosec (RSA)

Connect to 1st host - bastion host:
admin@server01:~/.ssh$ ssh -A admin@10.10.10.242
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-111-generic x86_64)

admin@server02:~$ ssh-agent
SSH_AUTH_SOCK=/tmp/ssh-gwx8Y2VklpbI/agent.26591; export SSH_AUTH_SOCK;
SSH_AGENT_PID=26592; export SSH_AGENT_PID;
echo Agent pid 26592;

If using SSH_AUTH_SOCK variable to add key:
    admin@server01:~$ ssh 10.10.10.242
    admin@10.10.10.242's password:
    
    admin@server01:~$ ssh admin@10.10.10.242
    admin@10.10.10.242's password:
    
    admin@server01:~$ SSH_AUTH_SOCK=/tmp/ssh-xlLGx8iT5DLr/agent.27033 ssh -A admin@10.10.10.242
    Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-111-generic x86_64)
    
    Last login: Fri Nov 13 12:31:24 2020 from 10.10.10.240
    admin@server02:~$
        ◊ This ssh command need -A so the key will be available to be used for ssh connection to 2nd host

Connect to 2nd host using the same key, works for both eval `ssh-agent -s` or SSH_AUTH_SOCK method above
admin@server02:~$ ssh 10.10.10.9
admin@10.10.10.9's password:

admin@server02:~$ ssh admin@10.10.10.9
Last login: Fri Nov 13 11:59:15 2020 from 10.10.10.242
You have logged into the system.
[Expert@fw-ch01-01:0]#
```

## ProxyJump and ProxyCommand

- Ssh -J <bastion host, bastion host> <remote host>
- https://www.redhat.com/sysadmin/ssh-proxy-bastion-proxyjump#:~:text=ProxyJump%20is%20the%20simplified%20way,the%20proxy%20or%20bastion%20hosts

## X11 Forwarding

- Server: /etc/ssh/sshd_config: X11Forwarding yes
    - Check if X11 Forwarding is enabled: sudo sshd -T | grep -i X11
- Client:
    - Windows: install XMing and enable X11 Forwarding in Putty
    - MacOS: install xquartz: brew install xquartz or from https://www.xquartz.org/
    - Command:
        - Run XMing or xquartz
        - For Xquartz right click and select terminal to use or set export DISPLAY=:0 before running SSH command below
        - SSH -X <user>@<host> or enable: ForwardX11 yes in ~/.ssh/config file. May have to use -Y instead of -X on some system
    - Checking if X11 Forwarding is enabled in SSH session: echo $DISPLAY
- Some Error:
    - See this: Error of failed request: BadAccess (attempt to access private resource denied) xclip
        - Solution: Use SSH -Y instead of -X
    - Warning: No xauth data; using fake authentication data for X11 forwarding
        - Solution: add to /etc/ssh/ssh_config of ssh client
        - MAC OS: XAuthLocation /opt/X11/bin/xauth
        - Linux: XAuthLocation /usr/bin/xauth

## Some Errors

### Too many authentication failure

- After checking everything is correct, but still get this one. The reason might be you are using RSA key file authentication and haveing ssh-agent sending multiple keys
- Solution is
    - adding -o IdentitiesOnly=yes or -oIdentitiesOnly=yes to ssh command
    - or adding to ~/.ssh/config file:
    ```bash
        Host *
        IdentitiesOnly=yes
    ```
- Reference: https://www.tecmint.com/fix-ssh-too-many-authentication-failures-error/

### Reference

https://www.howtoforge.com/reverse-ssh-tunneling
https://www.revsys.com/writings/quicktips/ssh-tunnel.html
https://vimeo.com/54505525
http://blog.pi3g.com/2013/05/raspberry-pi-socks-5-proxy-server-aka-browse-the-web-with-an-ip-from-a-different-country/
https://www.digitalocean.com/community/tutorials/how-to-route-web-traffic-securely-without-a-vpn-using-a-socks-tunnel
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