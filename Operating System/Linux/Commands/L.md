# ls
## List file with full time stamp
```bash
ls –time-style=full .
```

### Example
- List files in /usr/bin with modified time not by systemd, this is used to identify suspicious activity
```bash
ls -al –time-style=full /usr/bin | grep -v “00000\|->”
```