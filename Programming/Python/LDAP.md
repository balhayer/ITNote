# Search for entries
```python
import ldap3
server = ldap3.Server('10.10.10.248', get_info = ldap3.ALL, port =636, use_ssl = True)
connection = ldap3.Connection(server)
connection.bind()
connection.search(search_base='DC=intelligence,DC=htb', search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='*')
connection.entries
```

# Reference
- https://blog.thomastoye.be/python-ldap-authentication-with-microsoft-active-directory-46661bebc483