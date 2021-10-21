# Email freespace
```bash
#!/bin/bash

freespace=$(df -h | grep mapper | cut -d" " -f12)

if [[ $freespace > 70% ]]; then
        echo -e "Server Disk Free: $freespace\nClean up now to avoid failed backup" | mail -s "Server Disk Usage" -r networkoperations@domain.com recipient@domain.com
else
        echo "Free Space: $freespace"
fi
```