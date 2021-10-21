# Requests Module
## HTTP Put 
- PUT request is way different compared to POST request.
- With PUT request the file contents can be accessed using either request.data or request.stream. The first one stores incoming data as string, while request.stream acts more like a file object, making it more suitable for binary data:
```python
with open('uploaded_image.jpg', 'w') as f:
    f.write(request.stream.read())
```
