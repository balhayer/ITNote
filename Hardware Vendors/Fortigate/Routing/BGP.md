## Default information originate
```bash
config router bgp
    set as 65002
    set router-id 1.1.1.2
    config neighbor
        edit "1.1.1.1"
            set capability-default-originate enable
            set remote-as 65001

```

- This will advertise a default route to the BGP peer without a default route present in the RIB.  The default route will be created to be announced to the BGP neighbor only.

# Reference

- [BGP – default-originate-routemap purpose](https://kb.fortinet.com/kb/documentLink.do?externalID=FD45618)
- [Managing the ‘capability-default-originate’ BGP command](https://kb.fortinet.com/kb/documentLink.do?externalID=FD40370)
- [Use BGP Weight attribute to prefer default route received from neighbor over ‘capability-default-originate’ route](https://kb.fortinet.com/kb/documentLink.do?externalID=FD36488)