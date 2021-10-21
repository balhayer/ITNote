# Fortigate System Management

## Fortigate System Management Command
- get hardware status
- get system status
- get hardware memory
- get system performance status (run for 5 times)
- diagnose sys top 2 50 (run for 30 Sec and CTRL C to stop)
- diagnose sys top-summary
- diagnose sys top-summary '-n 50 -i 1 -s mem'
- diagnose sys session stat
- diagnose hardware sysinfo memory
- diagnose hardware sysinfo shm
- diagnose hardware sysinfo slab
- diagnose autoupdate versions
- diagnose ips memory status
- diagnose ips session status
- diagnose ips session list
- diagnose debug crashlog read

## Conserve Mode
- 3 memory thresholds : red, extreme and green
    - 'red' and 'extreme' : Both 'red' and 'extreme' are thresholds to enter in 'conserve mode' when the system memory used is over their thresholds.
        - When the used memory goes over the defined red threshold, the kernel raises the conserve mode state. FortiGate functions reacting to conserve mode state, like antivirus transparent proxies, would apply their own restriction based on their settings.
        - If used memory continues to increase and reach the 'extreme' threshold, conserve mode action taken with the red threshold are still active and additionally new sessions will be dropped.
    - 'green' : When used memory goes below the 'green' threshold, kernel releases the conserve mode state. FortiGate functions reacting to conserve mode state would stop their restriction measures.

### Configuration (CLI Only)
- Default values are : 
	- red : 88% of total memory  is considered "used memory"
	- extreme : 95% of total memory is considered "used memory"
 	- green : 82% of total memory is considered "used memory"
```bash
config system global
    set memory-use-threshold-extreme 95
    set memory-use-threshold-red 88
    set memory-use-threshold-green 82
end
```

### Verification Command
```bash
FGVM # diagnose hardware sysinfo conserve
memory conserve mode: off
total RAM:                            994 MB
memory used:                          448 MB   45% of total RAM
memory used threshold extreme:        944 MB   95% of total RAM
memory used threshold red:            874 MB   88% of total RAM
memory used threshold green:          815 MB   82% of total RAM
```

# Reference
- Diagnose sys top CLI Command: https://kb.fortinet.com/kb/documentLink.do?externalID=13825
- https://kb.fortinet.com/kb/documentLink.do?externalID=FD33103#:~:text=Proxy%20conserve%20mode%20is%20either,columns%20as%20diag%20sys%20top.
- https://kb.fortinet.com/kb/documentLink.do?externalID=FD45766
- https://kb.fortinet.com/kb/documentLink.do?externalID=FD49530
- https://social.technet.microsoft.com/Forums/office/en-US/dc4891be-e3ea-4321-972f-e66eee6ed1d1/how-does-a-root-ca-certificate-get-distributed-to-domain-clients?forum=winserversecurity
- [Tehnical Tip: Conserve mode changes](https://kb.fortinet.com/kb/documentLink.do?externalID=FD39790)