# Linux Capability
- Capabilities are assigned in sets, namely "permitted", "inheritable", "effective" and "ambient" for threads, and "permitted", "inheritable" and "effective" for files. 
- When setting capabilities on file, we will almost always use "permitted" and "effective", for example CAP_DAC_OVERRIDE+ep. Notice the +ep, which denotes the aforementioned sets.
- Five Capabilities set:
  - CapInh = Inherited capabilities: +i when setting cap
  - CapPrm = Permitted capabilities. For "capability-aware" app like ping, it can bring capability to the effective set from the permitted set -> just need +p when setting cap
  - CapEff = Effective capabilities. For "non-capability-aware app" like tcpdump, need to set effective capability -> need +ep when setting cap
  - CapAmb = Ambient capabilities set. Together with Inherited, can use to set environment (like running bash shell) so the process can get required capability from a list of set provided to environment. Capability-ware app will get needed set only, while non-capability-aware app will inherit all set. Ambient capability can't be set using setcap 
  - CapBnd = Bounding set: defines the upper level of available capabilities. Only the capabilities in the bounding set can be added to the inheritable set, which uses the capset() system call. If a capability is dropped from the boundary set, that process or its children can no longer have access to it.
  
## Commands
- There are two main tools, getcap and setcap which can respectively view and set these attributes.
  - On Debian and Ubuntu, these tools are provided by the libcap2-bin package, which can be installed with: apt install libcap2-bin
  - On CentOS and Fedora, the libcap package is needed: yum install libcap
  - On Arch Linux, they are provided by libcap as well: pacman -S libcap
- getcap -r /: search your whole file-system recursively to find out which capabilities are already set on the system 
- capsh --print: print capabilities
- sudo setcap 'net_cap_raw+ep' /bin/tcpdump
- setcap -r /path/to/file: remove all capabilities on a file
- capsh --print -- -c "/bin/ping -c 1 localhost": capabilities of an executable when running
- capsh --drop=cap_net_raw --print -- -c "/bin/ping -c 1 localhost": drop capabilities of an executable

### Get capabilities of process
```bash
grep Cap /proc/$procid/status
capsh --decode=$cap_string
or
getpcaps $Processid
```

## Example
- sudo setcap 'net_cap_raw+p' /bin/ping: set cap for ping
- sudo getcap /bin/ping: get cap
- sudo strace ping
- grep Cap /proc/$procid/status: get cap status of a process
```bash
$ grep Cap /proc/$BASHPID/status
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 0000003fffffffff
CapAmb: 0000000000000000
$ capsh --decode=0000000000000000
0x0000000000000000=  (No Capability)
~$ ps -ef | grep ping
admin   360680  360661  0 22:34 pts/5    00:00:00 ping google.com
admin   360752  360650  0 22:34 pts/4    00:00:00 grep --color=auto ping
$ grep Cap /proc/360680/status
CapInh: 0000000000000000
CapPrm: 0000000000002000
CapEff: 0000000000000000
CapBnd: 0000003fffffffff
CapAmb: 0000000000000000
$ capsh --decode=0000000000002000
0x0000000000002000=cap_net_raw (have capability)
```

### Resource
- man capability
- https://man7.org/linux/man-pages/man7/capabilities.7.html
- https://www.vultr.com/docs/working-with-linux-capabilities
- https://linux-audit.com/linux-capabilities-101
- https://blog.container-solutions.com/linux-capabilities-why-they-exist-and-how-they-work
- https://blog.pentesteracademy.com/linux-security-understanding-linux-capabilities-series-part-i-4034cf8a7f09