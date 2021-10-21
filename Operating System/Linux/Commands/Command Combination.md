# Conversion of number system in Linux shell
## Using double brackets with echo, print, printf

- To Decimal
```bash
echo $((2#00000001)) = 1
echo $((16#AB)) = 171
echo $((8#70) = 56
print $((8#70))
printf “%d\n” $((8#70)). %d = decimal
```

## Using obase,ibase and bc
```bash
Character in hex must be uppercase
echo “obase=10; ibase=16; AB” | bc
echo “obase=2; ibase=16; F” | bc
```

# Compare files
## Comm

- comm file1 file2
    - First column: Line not present in file1
    - Second column: line not present in file2
    - Third column: file present in both

## Diff

- diff file1 file2 [-u | -c]: unified or context format
    - -: line appears in first file only
    - +: line appears in second file only

## Vimdiff

- open multiple files in multiple vim windows
- do: gets changes from the other window into the current one
- dp: puts the changes from the current window into the other one
- ]c: jumps to the next change
- [c: jumps to the previous change
- C w: switches to the other split window.

# Combination usage of sed, awk, cut, paste, cat, echo, grep

## Combine each 2nd line to the line before it

### Original data
```bash
#cat 7003.txt | grep -A1 "up" | grep -v "\-\-"
GigabitEthernet0/0/0 is up, line protocol is up
  Internet protocol processing disabled
GigabitEthernet0/0/0.55 is up, line protocol is up
  Internet address is 10.10.10.10/30
GigabitEthernet0/0/0.56 is up, line protocol is up
  Internet address is 10.11.10.10/30
GigabitEthernet0/0/1 is up, line protocol is up
  Internet protocol processing disabled
GigabitEthernet0/0/1.1 is up, line protocol is up
  Internet address is 10.12.10.1/21
GigabitEthernet0/0/1.22 is up, line protocol is up
  Internet address is 10.13.10.1/24
GigabitEthernet0/0/1.23 is up, line protocol is up
  Internet address is 10.14.10.1/24
GigabitEthernet0/0/1.100 is up, line protocol is up
  Internet address is 10.15.10.1/24
Loopback0 is up, line protocol is up
  Internet address is 10.16.10.1/30
```

### Using AWK
```bash
#  cat 7003.txt | grep -A1 "up" | grep -v "\-\-" | awk 'NR%2{printf "%s ",$0;next;}1'
GigabitEthernet0/0/0 is up, line protocol is up   Internet protocol processing disabled
GigabitEthernet0/0/0.55 is up, line protocol is up   Internet address is 10.10.10.10/30
GigabitEthernet0/0/0.56 is up, line protocol is up   Internet address is 110.11.10.10/30
GigabitEthernet0/0/1 is up, line protocol is up   Internet protocol processing disabled
GigabitEthernet0/0/1.1 is up, line protocol is up   Internet address is 10.12.10.1/21
GigabitEthernet0/0/1.22 is up, line protocol is up   Internet address is 10.13.10.1/24
GigabitEthernet0/0/1.23 is up, line protocol is up   Internet address is 10.14.10.1/24
GigabitEthernet0/0/1.100 is up, line protocol is up   Internet address is 10.15.10.1/24
Loopback0 is up, line protocol is up   Internet address is 10.16.10.1/30
```

### Using Sed
```bash
#cat 7003.txt | grep -A1 "up" | grep -v "\-\-" | sed 'N;s/\n/ /'
GigabitEthernet0/0/0 is up, line protocol is up   Internet protocol processing disabled
GigabitEthernet0/0/0.55 is up, line protocol is up   Internet address is 10.10.10.10/30
GigabitEthernet0/0/0.56 is up, line protocol is up   Internet address is 110.11.10.10/30
GigabitEthernet0/0/1 is up, line protocol is up   Internet protocol processing disabled
GigabitEthernet0/0/1.1 is up, line protocol is up   Internet address is 10.12.10.1/21
GigabitEthernet0/0/1.22 is up, line protocol is up   Internet address is 10.13.10.1/24
GigabitEthernet0/0/1.23 is up, line protocol is up   Internet address is 10.14.10.1/24
GigabitEthernet0/0/1.100 is up, line protocol is up   Internet address is 10.15.10.1/24
Loopback0 is up, line protocol is up   Internet address is 10.16.10.1/30
```

### Using Paste
```bash
#  cat 7003.txt | grep -A1 "up" | grep -v "\-\-" | paste -d " " - -
GigabitEthernet0/0/0 is up, line protocol is up   Internet protocol processing disabled
GigabitEthernet0/0/0.55 is up, line protocol is up   Internet address is 10.10.10.10/30
GigabitEthernet0/0/0.56 is up, line protocol is up   Internet address is 110.11.10.10/30
GigabitEthernet0/0/1 is up, line protocol is up   Internet protocol processing disabled
GigabitEthernet0/0/1.1 is up, line protocol is up   Internet address is 10.12.10.1/21
GigabitEthernet0/0/1.22 is up, line protocol is up   Internet address is 10.13.10.1/24
GigabitEthernet0/0/1.23 is up, line protocol is up   Internet address is 10.14.10.1/24
GigabitEthernet0/0/1.100 is up, line protocol is up   Internet address is 10.15.10.1/24
Loopback0 is up, line protocol is up   Internet address is 10.16.10.1/30
```

## Extract 1 line and all indented lines below it

### Original data
```bash
Standard IP access list 1
    10 permit 211.81.116.123
    20 permit 211.81.116.68, wildcard bits 0.0.3.19 (19476 matches)
    30 permit 211.81.116.136, wildcard bits 0.0.3.19 (2 matches)
    40 permit 211.81.116.152, wildcard bits 0.0.0.3
    50 permit 211.81.122.68, wildcard bits 0.0.0.19
    60 permit 211.81.125.40, wildcard bits 0.0.0.7
    70 permit 211.81.126.60, wildcard bits 0.0.0.3
    80 permit 211.81.126.64, wildcard bits 0.0.0.7
    90 permit 120.150.5.164, wildcard bits 0.0.0.3
    100 permit 120.150.5.144, wildcard bits 0.0.0.15
    110 permit 120.150.5.140, wildcard bits 0.0.0.3
    120 permit 120.150.11.188, wildcard bits 0.0.0.1
Standard IP access list 2
    10 permit 192.143.9.1
    20 permit 192.168.4.20 (30019196 matches)
    30 permit 192.148.9.13
    40 permit 192.168.4.16, wildcard bits 0.0.0.15 (939568 matches)
    50 permit 192.143.0.0, wildcard bits 0.0.0.255
Extended IP access list Anti-Spoofing
    10 deny ip 192.150.8.0 0.0.7.255 any
    20 deny ip 192.150.16.0 0.0.7.255 any
    30 deny ip 192.150.24.0 0.0.7.255 any
    40 permit ip any any (969054186 matches)
Extended IP access list InboundTraffic
    10 permit ip 100.65.0.0 0.31.255.255 any
    20 permit ip 100.50.0.0 0.0.255.255 any
    30 permit ip any 192.143.244.0 0.0.0.255
    40 permit ip 192.148.0.0 0.1.255.255 192.150.16.0 0.0.15.255
    50 permit ip 192.143.0.0 0.0.127.255 192.150.16.0 0.0.15.255
    60 permit ip 192.168.0.0 0.0.63.255 192.150.16.0 0.0.15.255
    70 permit ip 192.143.234.0 0.0.0.255 192.150.16.0 0.0.15.255
    80 permit ip 10.6.0.0 0.0.255.255 192.150.16.0 0.0.15.255
    90 permit ip 192.17.96.0 0.0.7.255 192.150.16.0 0.0.15.255
    100 permit ip 10.32.96.0 0.0.7.255 192.150.16.0 0.0.15.255
    110 permit ip 192.164.64.0 0.0.15.255 192.150.16.0 0.0.15.255
    120 permit ip 192.182.16.0 0.0.15.255 192.150.16.0 0.0.15.255
    130 permit ip 192.123.24.0 0.0.7.255 192.150.16.0 0.0.15.255
    140 permit ip 192.123.160.0 0.0.7.255 192.150.16.0 0.0.15.255
    150 permit ip 192.124.64.0 0.0.7.255 192.150.16.0 0.0.15.255
    160 permit ip host 203.46.212.155 192.150.16.0 0.0.15.255
    170 permit tcp any 192.150.16.0 0.0.15.255 eq www 443 3269
    180 permit ip 192.17.7.0 0.0.0.255 192.150.16.0 0.0.15.255
    190 deny ip any any
Extended IP access list OutboundTraffic
    10 permit ip any any log
```

### Using AWK
```bash
#cat acl.txt | awk '/InboundTraffic/ && !f{f=1;x=$0;sub(/[^ ].*/,"",x);x=x" ";print;next} f {if (substr($0,1,length(x))==x)print; else f=0}'
Extended IP access list InboundTraffic
    10 permit ip 100.65.0.0 0.31.255.255 any
    20 permit ip 100.50.0.0 0.0.255.255 any
    30 permit ip any 192.143.244.0 0.0.0.255
    40 permit ip 192.148.0.0 0.1.255.255 192.150.16.0 0.0.15.255
    50 permit ip 192.143.0.0 0.0.127.255 192.150.16.0 0.0.15.255
    60 permit ip 192.168.0.0 0.0.63.255 192.150.16.0 0.0.15.255
    70 permit ip 192.143.234.0 0.0.0.255 192.150.16.0 0.0.15.255
    80 permit ip 10.6.0.0 0.0.255.255 192.150.16.0 0.0.15.255
    90 permit ip 192.17.96.0 0.0.7.255 192.150.16.0 0.0.15.255
    100 permit ip 10.32.96.0 0.0.7.255 192.150.16.0 0.0.15.255
    110 permit ip 192.164.64.0 0.0.15.255 192.150.16.0 0.0.15.255
    120 permit ip 192.182.16.0 0.0.15.255 192.150.16.0 0.0.15.255
    130 permit ip 192.123.24.0 0.0.7.255 192.150.16.0 0.0.15.255
    140 permit ip 192.123.160.0 0.0.7.255 192.150.16.0 0.0.15.255
    150 permit ip 192.124.64.0 0.0.7.255 192.150.16.0 0.0.15.255
    160 permit ip host 203.46.212.155 192.150.16.0 0.0.15.255
    170 permit tcp any 192.150.16.0 0.0.15.255 eq www 443 3269
    180 permit ip 192.17.7.0 0.0.0.255 192.150.16.0 0.0.15.255
    190 deny ip any any
```

## Print range of character from each line

- cut -c 1-N

# Reference

- https://unix.stackexchange.com/questions/184340/how-to-grep-a-line-with-unknown-number-of-its-indented-lines