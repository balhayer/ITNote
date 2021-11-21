# Components
- Master Node: Control plane, includes, API Server, Scheduler, etcd (storage) 
- Worker Node: Run pods
- Pod: unit of management of k8s, run containers (1 or more), but usually 1 app per pod
- IP: assigned to Pod, but changed when pod changes -> service
- Service: Permanent IP, doesn't change even when pod change
- ConfigMap: Mapping of all parameters, but not confidential parameter such as password, used by k8s to build cluster -> Secret
- Secret: contain confidential parameters
- Deployment: blueprint, in yaml or json format, to build cluster, define replica of an app, but not for database because of data inconsistency -> Statefulset
- Statefulset: like deployment but for database to ensure data consistency

# Sample Projects