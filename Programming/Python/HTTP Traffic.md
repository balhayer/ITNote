# Requests Module
## HTTP Put 
- PUT request is way different compared to POST request.
- With PUT request the file contents can be accessed using either request.data or request.stream. The first one stores incoming data as string, while request.stream acts more like a file object, making it more suitable for binary data:
```python
with open('uploaded_image.jpg', 'w') as f:
    f.write(request.stream.read())
```

## Download many files
```python
#!/usr/bin/python3

import requests
import os

url = 'http://intelligence.htb/documents/'

for i in range(2020,2022):
    for j in range(1,13):
        for k in range(1,31):
            date = f'{i}-{j:02}-{k:02}-upload.pdf'
            r = requests.get(url+date)
            if (r.status_code == 200):
                print (date)
                os.system('mkdir pdf')
                os.system(f'wget {url}{date} -O pdf/{date}')
```