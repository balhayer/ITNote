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