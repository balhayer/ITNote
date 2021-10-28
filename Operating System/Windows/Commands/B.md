# bitsadmin
	- bitsadmin /create /download <name>: create download job
	- bitsadmin /addfile <name create above> <http://...file.exe> <c:\local path\file.exe>
	- can add many files as it runs as batch job
	- check list: bitsadmin /list
	- start the job: bitsadmin /resume <job name above>
	- monitor jobs: bitsadmin /monitor
	- complete tasks and save files: bitsadmin /complete <job name above>
	- delete job: bitsadmin /reset
    - http://msdn.microsoft.com/en-us/library/aa362812(v=vs.85).aspx