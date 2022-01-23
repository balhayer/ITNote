# Certutil

## Used to decode hex

```bash
C:\>echo 48656c6c6f0a > poc.hex
or can use this to remove newline
C:\>echo|set /p="48656c6c6f0a" > poc.hex

C:\>certutil -f -decodeHex poc.hex poc.txt
Input Length = 15
Output Length = 6
CertUtil: -decodehex command completed successfully.

C:\>type poc.txt
Hello

C:\>type poc.hex
48656c6c6f0a
```

## Decode Base64
- certutil -decode file.b64 decoded.txt
