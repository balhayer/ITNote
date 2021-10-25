# Curl
## Options:

- -X: Method GET, POST, etc
- -F or –form: Form data
- -v: verbose
- -u: username:password
- -k, –insecure: allow insecure connection

## Upload file using Post:
```bash
curl -X POST -F "file=@./file.txt" -F "key=<key>" https://website.com/uploader
```

## Delete file from ftp server:
```bash
curl -v -u username:pwd ftp://host/FileTodelete.xml -Q 'DELE FileTodelete.xml'
curl -v -u username:pwd ftp://host/FileTodelete.xml -Q 'DELETE FileTodelete.xml'
curl -v -u username:pwd ftp://host/FileTodelete.xml -Q 'rm FileTodelete.xml'
```

## Using a proxy
```bash
curl --proxy socks5://127.0.0.1:8080 checkip.dyndns.org
```

## Testing SSL/TLS and cipher suite
```bash
curl https://10.0.0.5:10443 -k -v --location-trusted --sslv3: test ssl v3
curl https://10.0.0.1:443 -k -v --location-trusted --tlsv1.2 --ciphers 3DES: test tls1.2 and 3DES cipher
curl https://10.0.0.5:10443 -k -v --location-trusted --tlsv1.2 --ciphers AECDH-AES128-SHA
```
## Reference

- https://davidwalsh.name/curl-post-file
- https://medium.com/@petehouston/upload-files-with-curl-93064dcccc76
- https://kb.fortinet.com/kb/documentLink.do?externalID=FD37759