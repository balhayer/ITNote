# Find
## Options
- -type: f (file), d (directory)
- -name, -iname: specify name of file/case insensitive
- -size <size>: size of files, e.g.: +30k (> 30 KB), -1M (< 1 MB), 30c (= 1 Byte)
- -user: username of owner
- -perm: permission in octal (owner-group-others, 4=r, 2=w, 1=x, more info) or symbolic
- octal: 644 (exactly 644), -444 (at least readable by everyone, even when someone may have write permission), /666 (match any, readable and writable by at least one of the groups)
- symbolic: u=r
- time-related (-<prefix><word> <value>): words are min = minute, time = day; prefixes are a=accessed, m=modified, c=changed
- -amin +30: last accessed more than 30 mins ago
- -mtime -7: modified less than 7 days ago
- -mtime 0: last modified within the last 24 hours
- -exec: exec new command, e.g.: -exec ls -l {} \;

## Some Examples:

- find . -type f -empty: find empty file in current directory
- find /home -user someuser -mtime 7 -iname “.db”: find all .db files modified in the last 7 days by someuser
- find ./ -name “*file*” -printf ‘%T+ %p\n’: find file with name include some text in current folder, then print Time and Path of file
- find ./ -name “*file*” -printf ‘%T+ %p\n’ | sort -r | head -1: do the same, then sort in reverse order (latest first) and get the first one
- find * -newermt 2019-11-27 ! -newermt 2019-11-30 | xargs ls -alSt: find files between 27 and 29/11/2019 then list them pipe them to list in time order
- find * -newermt “2019-11-27 10:05:00” ! -newermt 2019-11-30 | xargs ls -alSt: same as above but include time value
- find * -newermt “2019-11-27 10:05:00” ! -newermt 2019-11-30 -exec ls -al \;: similar to above command, but use -exec instead of pipe
- find / -type f -user kittycat: find all files owned by the user “kittycat”
- find / -type f -size 150c: Find all files that are exactly 150 bytes in size
- find /home -type f -size -2k -name “*.txt”: Find all files in the /home directory (recursive) wtth size less than 2K and extension “*.txt”
- find / -type f -perm 644: find all files that are exactly readable and writeable by the owner, and readable by everyone else (use octal format)
- find / -type f -perm 444: find all files that are only readable by anyone (use octal format)
- find / -type f -perm o=w: find all files with write permission for the group “others” , (use symbolic format)
- find /usr/btn -type f -user root -perm u=s: find all files in the /usr/btn directory (recursive) that are owned by root and have at least the SUID permission (use symbolic format)
- find / -type f -name “*.png” -atime +10: find all files that were not accessed in the last 10 days with extension png
- find /usr/btn -type f -mmin 120: find all files in the /usr/btn directory (recursive) that have been modified within the last 2 hours

### Delete all folder in current directory, except logs folder:

- find . -type d ! -name logs | sudo xargs rm -rf

### Delete files/folder older than x days

- find ./ -mtime +550 -type d | xargs rm -rf

### List folder (-type d) older than 550 days (mtime – modification time)
- find ./ -mtime +550 -type d

### Delete them, will work with file (-type f)
```bash
find ./ -mtime +550 -type d -delete
find: cannot delete â./2017-10-10â: Directory not empty
find: cannot delete â./2017-10-13â: Directory not empty
find: cannot delete â./2017-10-20â: Directory not empty
find: cannot delete â./2017-10-11â: Directory not empty

Pipe them to command to remove:
find ./ -mtime +550 -type d | xargs rm
rm: cannot remove ‘./2017-10-10’: Is a directory
rm: cannot remove ‘./2017-10-13’: Is a directory
rm: cannot remove ‘./2017-10-20’: Is a directory
rm: cannot remove ‘./2017-10-11’: Is a directory

Recursive and force remove:
find ./ -mtime +550 -type d | xargs rm -rf

Those folders were removed:
find ./ -mtime +550 -type d

Newer folders are still available:
find ./ -mtime +500 -type d
./2017-12-8
./2017-11-17
./2017-11-10
./2017-12-1
./2017-10-27
./2017-11-24
./2017-11-3
```

## Find and sort files based on date

- https://www.ostechnix.com/find-sort-files-based-access-modification-date-time-linux/
### Find last 5 oldest files

- find <$folder> -type f -printf ‘%T+ %p\n’ | sort | head -n 5

## Find files based on Permission

### Mode
- If we specify the mode without any prefixes, it will find files of exact permissions.
- If we use “-“ prefix with mode, at least the files should have the given permission, not the exact permission. OR operator
- If we use “/” prefix, either the owner, the group, or other should have permission to the file. AND operator

### Examples
- Find / -perm 777: find files with permission of exactly 777
- Find / -perm -766: find files with permission of at least 766 (so 777 should be included)
- Find / -perm /222: find files writable by someone (either user, group or other)
- Find / -perm /220: find files writable by either user or group, don’t have to match both
- Fine / -perm -220: find files writable by both user and group
- find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null: find all file with sticky bit set in user or group
- Reference: https://www.ostechnix.com/find-files-based-permissions/

## Find and compare md5 hash with 2 files have only 1 characters different (0 and 1)

- Find . -type f -exec md5sum {}\; | sed ‘s/\.[01]//g’

## Find file and print details per format

- find / -printf “%f\t%p\t%u\t%g\t%m\n” 2>/dev/null | column -t
    - \t: tab
    - %f: file name
    - %p: path
    - %u: user
    - %g: group
    - %m: permission
    - Column -t: print in column with tab, need \n in printf of find command

## Find files older than n days and delete

- find /opt/backup -type f -mtime +30 -delete: find and delete files older than 30 days
- find /var/log -type d -mtime +30 -exec rm -rf {} \;: Find and delete folder recursively older than 30 days. Using the -delete option may fail, if the directory is not empty.

## Some Other commands

- find / -user <user> -readable 2> /dev/null

## Reference:

- https://www.linode.com/docs/tools-reference/tools/find-files-in-linux-using-the-command-line/
- https://linuxacademy.com/blog/linux/the-linux-find-command/
- http://wisercoder.com/knowing-difference-mtime-ctime-atime/