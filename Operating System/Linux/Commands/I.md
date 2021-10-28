# IP link
## Disable arp
- ip link set <device> arp [on | off]
## Reference
- https://phoenixnap.com/kb/linux-ip-command-examples


# Iperf
## Installation On Ubuntu 64bit

- sudo apt remove iperf3 libiperf0
- sudo apt install libsctp1
- wget https://iperf.fr/download/ubuntu/libiperf0_3.9-1_amd64.deb
- wget https://iperf.fr/download/ubuntu/iperf3_3.9-1_amd64.deb
- sudo dpkg -i libiperf0_3.9-1_amd64.deb iperf3_3.9-1_amd64.deb
- rm libiperf0_3.9-1_amd64.deb iperf3_3.9-1_amd64.deb

## Server:

- Iperf -s [-p <$port>]: running as server
- Iperf -s -u: running as server in udp mode

## Client:

- Iperf -c [-p <$port>]
- Iperf -c <$server ip> -u
- Iperf -c <$server ip> -d: client run in client mode first then in server mode to test reverse direction

## Example:

- Server: iperf -s
- Client: iperf -c <$server address> -P 6 -t 600 -d: run 6 parallel test for 10 mins bidirectionally

## Options:

- -f: change format of bandwidth such as -f k for Kbits, options are m (Mbits), k (Kbits), K (Kbytes) and M (Mbytes)
- -i: interval between bandwidth test, -i 60 to report bandwidth every 60s
- -p: Change port, default is 5001, used both on client and server
- -B: Bind iPerft to specific interface or address
- -t: specify run time
- -P: process to run simultaneously
- -d: bidirectionally

## Running on Docker

### Server:

- docker run  -it --rm --name=iperf3-server -p 5201:5201 networkstatic/iperf3 -s

### Client:

- docker run  -it --rm networkstatic/iperf3 -c <$Server IP>
## Reference:

- https://iperf.fr/iperf-download.php
- https://hub.docker.com/r/networkstatic/iperf3/