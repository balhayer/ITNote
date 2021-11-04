# URL Decoding
```bash
function urldecode() {
    echo -ne $(echo -n "$1" | sed -E "s/%/\\\\x/g"
}    
```