# Invoke-Command
## Error WinRM client cannot process the request
- If seeing this error:
```bash
[10.1.1.1] Connecting to remote server 10.1.1.1 failed with the following error message : The WinRM client cannot process the request. If the authentication scheme is different from 
Kerberos, or if the client computer is not joined to a domain, then HTTPS transport must be used or the destination machine must be added to the TrustedHosts configuration setting. Use 
winrm.cmd to configure TrustedHosts. Note that computers in the TrustedHosts list might not be authenticated. You can get more information about that by running the following command: winrm 
help config. For more information, see the about_Remote_Troubleshooting Help topic.
    + CategoryInfo          : OpenError: (10.1.1.1:String) [], PSRemotingTransportException
    + FullyQualifiedErrorId : ServerNotTrusted,PSSessionStateBroken
```
- Enable Winrm service: start-service winrm
- And set trusted host to be *: Set-Item WSMan:localhost\client\trustedhosts -value * -Force
- Then run command: Invoke-command -computername $ip -credential $Credential -ScriptBlock {command}
- Example: 
```powershell
$r=Invoke-command -computername $ip -credential $Credential -ScriptBlock {ping -c 1 8.8.8.8}
Write-Host $r
```
## Reference
- https://www.dtonias.com/add-computers-trustedhosts-list-powershell/

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