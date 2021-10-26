# Troubleshooting
## BGP doesn't install a route
- Synchronization is enabled and route is not known via IGP
- Next Hop is unreachable
- AS_Path include local AS
- Attempting to readvertise iBGP-learned routes to iBGP neighbors
- Rejected by Inbound Policy
### Reference
- https://packetlife.net/blog/2008/nov/19/probable-reasons-bgp-isnt-installing-route/