## FTP Active vs Passive
### Protocol Operation

#### Active

- Client connects from random port > 1024 to server on port 21 for control channel
- Client use PORT command to specify client side port server should connect to for data channel
- Server connection from port 20 to client on the port specify by PORT command from client for data channel

#### Passive

- Client connects from random port > 1024 to server on port 21 for control channel
- Instead of using PORT command, client use PASV command to request server port to connect to for data channel
- Server replies with a port it’s listening for data channel
- Client connect to that port

### Firewall Consideration

#### For active mode
- Client side firewalls need to allow incoming connection from server
- Server side firewalls have to allow connections to random ports 1024-65535 if it can’t understand FTP to open port appropriately

#### For passive mode
- Server side firewalls have to allow connection from client to random ports. But this is easier as most fpt servers support to specify the range of passive mode ports to listen.
- Client side firewalls have to allow connections to random ports 1024-65535 if firewall can’t understand FTP to open port appropriately

## Reference

- https://www.jscape.com/blog/bid/80512/active-v-s-passive-ftp-simplified
- https://documentation.meraki.com/MX/NAT_and_Port_Forwarding/Active_and_Passive_FTP_Overview_and_Configuration