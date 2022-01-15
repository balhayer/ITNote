# Accessing Remote Powershell
```Powershell
$cred = Get-Credential
Enter-PSSession -ComputerName $remoteIP -Credential $cred
```

# Can't Accessing Remote Powershell from Linux
```powershell
PS /home/kali> enter-pssession -computername 10.10.10.237 -credential $cred -authentication negotiate
Enter-PSSession: Connecting to remote server 10.10.10.237 failed with the following error message : acquiring creds with username only failed Unspecified GSS failure.  Minor code may provide more information SPNEGO cannot find mechanisms to negotiate For more information, see the about_Remote_Troubleshooting Help topic.

PS /home/kali> sudo apt install gss-ntlmssp
[sudo] password for kali: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  cryptsetup-run gstreamer1.0-pulseaudio libgeos-3.9.0 python3-gevent
  python3-gevent-websocket python3-greenlet python3-jupyter-core python3-m2crypto
  python3-nbformat python3-parameterized python3-plotly python3-zope.event
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  gss-ntlmssp
0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
Need to get 47.6 kB of archives.
After this operation, 136 kB of additional disk space will be used.
Get:1 http://kali.download/kali kali-rolling/main amd64 gss-ntlmssp amd64 0.7.0-4 [47.6 kB]
Fetched 47.6 kB in 2s (23.9 kB/s)     
Selecting previously unselected package gss-ntlmssp.
(Reading database ... 296011 files and directories currently installed.)
Preparing to unpack .../gss-ntlmssp_0.7.0-4_amd64.deb ...
Unpacking gss-ntlmssp (0.7.0-4) ...
Setting up gss-ntlmssp (0.7.0-4) ...
Processing triggers for man-db (2.9.4-2) ...

Try again: 
PS /home/kali> enter-pssession -computername 10.10.10.237 -credential $cred -Authentication negotiate
[10.10.10.237]: PS C:\Users\Administrator\Documents>
```