# Invoke-WebRequest
```bash
Invoke-WebRequest [-uri] <url>
iwr [-uri] <url>
curl [-uri] <url>
```

## Some Errors

### Exception: The underlying connection was closed
```bash
iwr : The underlying connection was closed: An unexpected error occurred on a send.
At line:1 char:1
+ iwr -uri "https://<url> ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-WebRequest], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeWebRequestCommand
```
#### Solution: Enable all TLS versions
```bash
 [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls -bor [Net.SecurityProtocolType]::Tls11 -bor [Net.SecurityProtocolType]::Tls12 
```

## Reference

https://blog.darrenjrobinson.com/powershell-the-underlying-connection-was-closed-an-unexpected-error-occurred-on-a-send/
https://davidhamann.de/2019/04/12/powershell-invoke-webrequest-by-example/