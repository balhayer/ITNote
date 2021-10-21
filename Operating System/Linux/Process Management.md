# Process Management
## Backgrounding a Process

- Add & to the end of command
- Running command without & and use bg command to send it to background

## List Jobs and Bring process to foreground

- jobs: list all current running jobs in current session
- fg [%<id>|<beginning of name of process>]: bring process to foreground
    - %+: current job
    - %-: previous job

## Process Control

- ps: see process status, system wide, not of current session like jobs
    - -e: all process
    - -f: full format listing
    - -C <command name>: select command name
- kill <pid>: kill process