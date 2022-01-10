# IPv4 Fragmentation, MTU, MSS, PMTUD
## Fortigate Devices – honor-df settings

- By default, Fortigate respect the do-not-fragment bit in packet which is defined as honor-df enable. This can cause problem to the network if traffic needs to be fragmented
- Change global config
```bash
config global (just need for multivdom mode)
  config system global
    set honor-df disable
```

# Reference
- https://community.fortinet.com/t5/FortiGate/Technical-Tip-Global-setting-honor-df-explained/ta-p/197002?externalID=FD51964
- https://www.cisco.com/c/en/us/support/docs/ip/generic-routing-encapsulation-gre/25885-pmtud-ipfrag.html