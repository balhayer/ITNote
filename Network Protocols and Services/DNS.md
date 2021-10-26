## Flush DNS Cache

### Windows:
- ipconfig /flushdns
### MacOS:
- Big Sur: sudo dscacheutil -flushdns; sudo killall -HUP mDNSResponder
### Linux:
- Local NSCD DNS Cache: sudo /etc/init.d/nscd restart
- Local dnsmasq DNS cache: sudo /etc/init.d/dnsmasq restart
- Local BIND DNS Cache:
    - sudo /etc/init.d/named restart
    - sudo rndc restart or sudo rndc flushname <domain.com>
    - sudo rndc exec
### Reference:
- https://linuxhint.com/flush_dns_cache_ubuntu/
- https://phoenixnap.com/kb/how-to-flush-dns-cache