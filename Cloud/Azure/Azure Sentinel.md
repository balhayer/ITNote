# Fortinet Connector

- Following instruction for fortinet connector, it requires a CEF collector installed on Linux machine which receive syslog message in CEF format from fortigate, it then forward this log to Azure Sentinel using shared keys
## Configuration on Fortinet to send logs to CEF collector
```bash
config log syslogd setting
    set status enable
    set server "IP of CEF collector"
    set source-ip "Source IP"
    set format cef
end
```
# Reference

- https://docs.microsoft.com/en-us/azure/sentinel/connect-common-event-format#security-considerations
- https://docs.microsoft.com/en-us/azure/azure-monitor/agents/agent-windows?WT.mc_id=Portal-fx#obtain-workspace-id-and-key