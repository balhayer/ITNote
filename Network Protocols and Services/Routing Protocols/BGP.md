# BGP and Route Objects
- Most international transit providers are trying to take actions to mitigate route hijacking.
- Route object will help to pass through any security mechanisms imposed by  ISPs and other Transit Providers.

## Configuration
- Login to portal of Internet Address Registry that manages AS number such as APNIC

## Verification
- whois -h whois.apnic.net 103.113.1.0

## Reference

- https://blog.apnic.net/2019/09/11/how-to-creating-rpki-roas-in-myapnic/
- https://www.apnic.net/wp-content/uploads/2017/01/route-roa-management-guide.pdf

# Troubleshooting
## BGP doesn't install a route
- Synchronization is enabled and route is not known via IGP
- Next Hop is unreachable
- AS_Path include local AS
- Attempting to readvertise iBGP-learned routes to iBGP neighbors
- Rejected by Inbound Policy
### Reference
- https://packetlife.net/blog/2008/nov/19/probable-reasons-bgp-isnt-installing-route/