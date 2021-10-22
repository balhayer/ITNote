# Ansible Logging
- By default, Ansible doesn’t log anything, information is written to STDOUT
    - log_path=<filename>: set default secion of ansible.cf to force writing log files
    - or set $ANSIBLE_LOG_PATH environmental variable
- Make sure to configure logrotate on ansible log files