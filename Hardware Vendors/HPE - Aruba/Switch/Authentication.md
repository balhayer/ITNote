## Aruba AOS-CX local user role

```bash
user configbk authorized-key ssh-rsa AAAAB3Nz.....KxvePINAvd
user-group backups
    10 permit cli command "show run"
    20 permit cli command "show version"
    30 permit cli command "show module"
    40 permit cli command "show interface"
    50 permit cli command "show system"
    60 permit cli command "show environment"
    70 permit cli command "no page"
user configbk group backups password ciphertext AQB...1oZwB6m
```
