# wevtutil

	- Enables you to retrieve information about event logs and publishers, install and uninstall event manifests, run queries, and export, archive, and clear logs.
	- Must have administrative roles to run
	- wevtutil el: list all logs on the system
	- wevtutil gli Security: Stat of security logs
	- wevtutil qe Security /c:3 /rd:true /f:text: display 3 last entries in text in security logs
	- wevtutil epl Security c:\demo.evtx: export events
	- wevtutil cl Security /bu:c:\SecurityLogBackup.vtx: clear log and backup before clearing
    - CLI Reference: https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc732848(v=ws.11)?redirectedfrom=MSDN

# WMI
