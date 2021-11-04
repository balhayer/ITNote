# URL Decoding
```python
#Using urllib module
python3 -c 'u="<$urlencode>";import urllib.parse as ul; print(ul.unquote(u))'
#Using requests module
python3 -c 'u="<$urlencode>";import requests.utils as ul; print(ul.unquote(u))'
```