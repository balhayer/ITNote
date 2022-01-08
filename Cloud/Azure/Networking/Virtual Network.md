# Network Security Group (NSG)
## Intra-Subnet traffic
- It's important to note that security rules in an NSG associated to a subnet can affect connectivity between VM's within it. For example, if a rule is added to NSG1 which denies all inbound and outbound traffic, VM1 and VM2 will no longer be able to communicate with each other. Another rule would have to be added specifically to allow this.
- You can easily view the aggregate rules applied to a network interface by viewing the effective security rules for a network interface. You can also use the IP flow verify capability in Azure Network Watcher to determine whether communication is allowed to or from a network interface. IP flow verify tells you whether a communication is allowed or denied, and which network security rule allows or denies the traffic.
- https://docs.microsoft.com/en-us/azure/virtual-network/network-security-group-how-it-works

# Service Endpoint
- Created for VNet
- IP used for accessing other services will be Private instead of Public
- IP of other services such as VM access to Storage is still public (IP for Storage)
- Free 
- https://www.youtube.com/watch?v=q8s-zmHighs

# Private Endpoint
- https://www.youtube.com/watch?v=uBN3AVARUiI
- Service Endpoint vs Private Endpoint: https://www.youtube.com/watch?v=4v-9zGHxVeI