# Hairpin NAT on Mikrotik
## Scenario

- LAN: 192.168.0.0/24
- WAN Public IP: 100.100.100.100
- Server on LAN listen on port: TCP 4443

## Create Address for LAN subnet
```bash
/ip address 
print
add address=192.168.0.0/24 list=LAN
add address=100.100.100.100 list=WAN
```

## Mark Connection for Hairpin NAT
```bash
/ip firewall
print
chain=prerouting action=mark-connection new-connection-mark=Hairpin NAT passthrough=yes src-address-list=LAN dst-address-list=WAN
```

## Perform Hairpin NAT
```bash
/ip firewall nat
print
chain=srcnat action=masquerade connection-mark=Hairpin NAT
```

## Configure Port Forwarding
```bash
/ip firewall nat
print
chain=dstnat action=dst-nat to-addresses=192.168.0.100 to-ports=4443 protocol=tcp dst-address-list=WAN dst-port=443
```

## Reference
- https://forum.mikrotik.com/viewtopic.php?t=172380