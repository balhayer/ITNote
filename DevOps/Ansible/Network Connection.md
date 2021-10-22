# Managing network connection with Ansible
- Two variables are used to configure network role:
    - network_provider: typically set to nm
    - network_connections: specifies details about network connection
- Defaults for thse variables are set in /usr/share/ansible/roles/rhel-system-roles.network

## Module for Network Management

- nmcli: manage parameters for network devices and connections
- hostname: set name of a managed host
- firewalld: manage firewalld rules

### Gather some facts:

- ansible all -m setup -a ‘gather_subset=network filter=ansible_interfaces’
```bash
---
- name: setup a NIC
  hosts: server2
  tasks:
  - name: configure ens224
    nmcli:
      conn_name: LAN
      ifname: ens224
      type: ethernet
      ip4: 10.0.0.1/24
      state: present
  - name: set hostname
    hostname:
      name: server2.domain.com
  - name: move ens224 to internal zone
    firewalld:
      zone: internal
      interface: ens224
      permanent: yes
      state: enabled
  - name: enable http in firewall internal zone
    firewalld:
      zone: internal
      service: http
      permanent: yes
      state: enabled
```