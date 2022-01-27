# CSV File
- https://www.cyberciti.biz/faq/unix-linux-bash-read-comma-separated-cvsfile/

# Add content to many files
```bash
#!/bin/bash
folder="/storage/threatfeed/"
files=$(find $folder -name StaffAllow.txt)
exclude=$(grep -R -l $1 $folder | grep Staff | cut -f4 -d/)
change="no"
for f in $files
do
	for e in $exclude
	do
		if [[ "$f" == *"$e"* ]];
		then
			change="no"
			break
		else
			change="yes"
			#echo "*.instagram.*" $f
			#echo "*.twitter.*" $f
		fi
	done

	if [[ "$change" == "yes" ]]
	then
		echo "" >> $f
		echo "*.$1.*" >> $f
	fi
done
#Then Remove all empty line: find /storage/threatfeed/ -name StaffAllow.txt | xargs sed -is /^$/d
```
