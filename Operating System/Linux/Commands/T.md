# TCPdump
## Commands

- Read pcap file: tcpdump -r file.pcap
- Skip DNS lookup: tcpdump -n -r file.pcap
- Print packet in HEX and ASCII format: tcpdump -X -r file.pcap
- Write to pcap file: tcpdump -w file.pcap
- Some filters:
    - tcpdump src host 192.168.1.1 -r file.pcap
    - tcpdump dst host 192.168.1.1 -r file.pcap
    - tcpdump port 81 -r file.pcap

## TCP Header
```bash
    0                   1                   2                   3   
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |          Source Port          |       Destination Port        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                        Sequence Number                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Acknowledgment Number                      |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |  Data |       |C|E|U|A|P|R|S|F|                               |
    | Offset|  Res. |W|C|R|C|S|S|Y|I|            Window             | 
    |       |       |R|E|G|K|H|T|N|N|                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |           Checksum            |         Urgent Pointer        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Options                    |    Padding    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                             data                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

- Find all traffic with TCP port > 1024: tcpdump -i eth1 ‘tcp[0:2] > 1024’

## TCP Flags

- Is 13 bytes (count from 0) in a TCP header
- Flags: URG, ACK, PUSH, RST, SYN, FIN; which corresponds to 32 16 8 4 2 1.
- Mnenomic for those flags is Unskilled Attacker Pester Real Security Folks

### Example of using TCP Flags in TCPDump:

- Find all SYN packets:
    - tcpdump ‘tcp[13] & 2!=0’
    - tcpdump ‘tcp[13] & 2==2’
- Find all RST packets:
    - tcpdump ‘tcp[13] & 4!=0’
    - tcpdump ‘tcp[13] & 4==4’
- Find all ACK packets:
    - tcpdump ‘tcp[13] & 16!=0’
    - tcpdump ‘tcp[13] & 16==16’
- Find all SYN-ACK packets:
    - tcpdump ‘tcp[13]=18’

## Reference
- https://danielmiessler.com/study/tcpflags/

# Tshark
## Installation

- sudo add-apt-repository ppa:wireshark-dev/stable
- sudo apt-get install wireshark tshark
- sudo apt-cache madison tshark
- sudo dpkg-reconfigure wireshark-common: reconfigure normal user to capture packet
    - sudo usermod -a -G wireshark $USER
    - newgrp wireshark: activate wireshark group
    - id to check
- Default behavior:
    - only capture unicast, broadcast and multicast
    - check using: ifconfig
    - Change to promiscuous mode: ifconfig <$int> [-]promisc (- to disable)

## Options:

- -D: list interface
- -i {any|interface name|number from -D}: capture on any interface
- -c <$num of packets to capture>
- -w <.pcap file to write>
- -r: <.pcap file to read>
- -V: see details of packet
    - tshark -r capture.pcap -c 1 -V
- -T <$format>:
    - tshark -T x: just invalid variable to get help about -T
    - tshark -r capture.pcap -T psml > capture.psml
- -b filesize:<$KBytes> -b files:<$num_of_file> : buffer
- -d: decode as protocol use non-standard port
    - tshark -d .: get help
    - Case Study: SIP-TLS + RTP
    - VoIP Traffic: SIP over TLS but RTP not encrypted
    - Tshark and other tools depend on SIP to decode RTP: Rely on SDP packets which are encrypted
    - Assist Tshark/Wireshark by decoding UDP as RTP
    - tshark -r voice.pcap -Y “udp.port=4000” -d udp.port==4000,rtp
- -G: preference
    - tshark -G help: get help
    - tshark -G currentprefs | grep ssl
- -o “ssl.keys_list:0.0.0.0,443,http,<$keyfile>”: SSL Decryption
    - tshark -r HTTPStraffic.pcap -o “ssl_keys_list:0.0.0.0,443,http,private.key”

## Conversion

- installation: sudo apt install xsltproc
- from xml to html:
    - tshark -r capture.pcap -T pdml > icmp.xml
    - xsltproc /user/share/wireshark/pdml2html.xsl icmp.xml > icmp.html

- ## Filter

- -f <$filter>: capture filter
    - tshark -I ens33 -c 4 -f “tcp port 80” -w tcp80.pcap
    - https://www.wireshark.org/docs/man-pages/pcap-filter.html
- -Y ‘<$filter>’: display filter
    - tshark -r capture.pcap -Y ‘http.request.method==”GET”‘
    - https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html
    - https://www.wireshark.org/docs/dfref

## Extract Data

- -Tfields -e <$expression>: filter specific header/information
    - tshark -r wireless.pcap -Y ‘wlan.fc.type_subtype==0x0008’ Tfields -e ‘wlan.ssid’
        - -Y ‘wlan.fc.type_subtype==0x0008’: beacon packet
    - tshark -r capture.pcap -Y ‘http.request.method==”GET”‘ -Tfields -e http.post -e http.request.uri

## Summary/Statistics:

- -z <$filter>: statistics
    - tshark -z help
    - tshark -r capture.pcap -z io,phs: show statistics after showing all packet
    - tshark -r capture.pcap -q -z io,phs: show statistics without showing packet details
    - tshark -r capture.pcap -q -z io,phs,’wlan.bssid==<mac address of AP>’: show statistics for specific AP
    - or tshark -r capture.pcap -R ‘wlan.bssid==<mac of AP>’ -q -z io,phs: show statistics for specific AP
    - tshark -r wireless.pcap -q -z endpoints,<wlan|tcp|udp>
    - tshark -r wireless.pcap -q -z endpoints,wlan,’wlan.bssid==<mac of AP>’
    - tshark -r wireless.pcap -q -z conv,ip (conversion ip)
    - tshark -r wireless.pcap -q -z expert: expert information
    - tshark -r httptraffic.pcap -q -z http.tree
    - tshark -r voice.pcap -q -z sip.stat
    - tshark -r voice.pcap -q -z rtp.streams
    - tshark -r voice.pcap -q -z follow,tcp|udp

## Online tool to read file

- xmlgrid.net
- jsonformatter.org


# Tmux
## Installation

- apt-get install tmux
- Configuration file: ~/.tmux.conf
- set-option -g mouse on: enable mouse support
- set-option -g history-limit 3000: set history limit
- After making change: source-file ~/.tmux.conf

Commands

- Windows and Pane: Command ctrl_b, then:
    - c: create window
    - , (comma): rename window
    - p|n|<number of window>: previous|next window
    - w: list windows
    - %: split windows
    - ” (double quote) | :split-windows: split horizontally
    - ?: help
    - <> (left, right arrow): change between panels
    - Ctrl_<> to resize panel
    - <space>: change panel layout
    - { }: move panel around
    - [: copy mode
        - Move up/down, then Ctrl_<space> to start highlight, then move cursor
        - <Enter> or Alt_w (Esc_w on Mac) to copy text to tmux clipboard
        - Ctrl_b, ] to paste
        - q to quit
    - t: show time panel, q for quit
    - q: to show number of panel, <number> to jump to that panel
    - :join-pane -s <windows>.<pane>
    - z: zoom/unzoom a pane
    - x|&: force kill all unresponsive process in a pane|window
    - L (lower case L): switch to last used windows
- Alt_. (dot): cycle through last word of previous commands
- Session
    - tmux new -s <name>: Create new session
    - Ctrl_b, d: detach session
    - tmux ls | list-sessions: list tmux sessions
    - tmux attach [-t <session name>]: re-attach session
    - <prefix> (|): previous | next session
- Tmux list-keys = Ctrl_b,? : see all hot keys
- Note:
    - Paste in vi editor: hold shift and right mouse click
- Capture pane content to file:
    - Ctrl_b, :
    - Capture-pane -b <buffername> -S -: -S – Start of history
    - Save-buff -b <buffername> <file>
    - https://blog.sleeplessbeastie.eu/2019/10/28/how-to-store-the-contents-of-tmux-pane/
    - https://ricochen.wordpress.com/2011/04/07/capture-tmux-output-the-much-less-painful-way/

## Reference
- https://www.linode.com/docs/networking/ssh/persistent-terminal-sessions-with-tmux/
- https://gist.github.com/russelldb/06873e0ad4f5ba1c4eec1b673ff4d4cd