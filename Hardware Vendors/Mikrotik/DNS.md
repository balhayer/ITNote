# Conditional Forwarding DNS in Mikrotik
- Mikrotik doesn’t have an official way to configure conditional DNS. The following layer 7 rule and nat will forward dns request for specific dns domain to specified dns server
    - 192.168.0.1: LAN IP of Mikrotik, configured as DNS server for local clients
    - domain.com: domain that need conditional dns forwarding
    - 10.0.0.1: dns server that serve queries for domain.com

```bash
/ip firewall layer7-protocol add name=domain.com regexp=domain.com

/ip firewall mangle add chain=prerouting dst-address=192.168.0.1 layer7-protocol=domain.com action=mark-connection new-connection-mark=domain.com-forward protocol=tcp dst-port=53

/ip firewall mangle add chain=prerouting dst-address=192.168.0.1 layer7-protocol=domain.com action=mark-connection new-connection-mark=domain.com-forward protocol=udp dst-port=53

/ip firewall nat add action=dst-nat chain=dstnat connection-mark=domain.com-forward to-addresses=10.0.0.1

/ip firewall nat add action=masquerade chain=srcnat connection-mark=domain.com-forward
```

## Reference:
- https://blog.johannfenech.com/mikrotik-conditional-dns-forwarding