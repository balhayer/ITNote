# VSFTPD
## Installation on Ubuntu Server

- sudo apt-get install vsftpd

## Configuration

### Configuration file is in /etc/vsftpd.conf
```bash
# Allow local users to log in.
local_enable=YES
#
# Allow Upload
write_enable=YES
# Local user will not be allow to change to a folder different from their home folder
chroot_local_user=YES 
# You may specify an explicit list of local users to chroot() to their home
# directory. If chroot_local_user is YES, then this list becomes a list of
# users to NOT chroot().
chroot_list_enable=YES
#This is a security risk because to allow user to logon there's no way to limit that same user from ssh
#If set their shell to /bin/nologin, they will not be able to login FTP
```

### Enable virtual users

- Create system user to map to virtual users: useradd -d /storage/ftproot vftpuser
- Configuration file: /etc/vsftpd/vsftpd.conf
```bash
listen=NO
listen_ipv6=YES
anonymous_enable=NO
ftpd_banner="Some Banner"
local_enable=YES
write_enable=YES
guest_enable=YES
guest_username=vftpuser
virtual_use_local_privs=YES
user_sub_token=$USER
local_root=/storage/ftproot/$USER
allow_writeable_chroot=YES
user_config_dir=/etc/vsftpd/userconf
chroot_local_user=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
```

- User specific configuration: /etc/vsftpd/userconf/global (different config), if not needed, user folder will be /storage/ftproot/<user>
```bash
local_root=/storage/ftproot/
write_enable=YES
```

- PAM configuration: /etc/pam.d/vsftpd
```bash
Passwords are generated using openssl command
auth	required	pam_pwdfile.so debug pwdfile=/etc/vsftpd/passwd
account required	pam_permit.so

Passwords are generated using text file and db_load
auth	required 	pam_userdb.so	db=/etc/vsftpd/users	
account	required 	pam_userdb.so	db=/etc/vsftpd/users
```
- Generating password
    - Using openssl: openssl passwd -1 , then copy generated password to password in this format
```bash
<user>:<generate password hash>
```
    - Using db_load: create text file as following
```bash
user1
password1
user2
password2
Then, encrypt it using db_load -T -t hash -f users.txt /etc/vsftpd/users.db
```

- Permission for ftp root should be
```bash
ls -al /storage/ftproot/
total 28
drwxrwxr-x 3 vftpuser vftpuser 4096 Jul 12 22:12 .
drwxr-xr-x 4 root  root  4096 Jul 12 19:46 ..
drwxr-xr-x 2 vftpuser vftpuser 4096 Jul 12 19:23 <folder>
-rw-rw-r-- 1 vftpuser vftpuser    1 Jul  7 13:35 file1.txt
-rw-rw-r-- 1 vftpuser vftpuser    1 Jul  7 13:35 file2.txt
-rw-rw-r-- 1 vftpuser vftpuser   49 Jul  7 00:16 index.html
-rw-rw-r-- 1 vftpuser vftpuser    1 Jul  7 13:35 file3.txt
```

## Verification

- sudo systemctl {status | restart | stop | start } vsftpd.service
```bash
vsftpd.service - vsftpd FTP server
     Loaded: loaded (/lib/systemd/system/vsftpd.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2021-07-12 22:21:47 AWST; 2h 25min ago
    Process: 6039 ExecStartPre=/bin/mkdir -p /var/run/vsftpd/empty (code=exited, status=0/SUCCESS)
   Main PID: 6046 (vsftpd)
      Tasks: 7 (limit: 9448)
     Memory: 4.8M
     CGroup: /system.slice/vsftpd.service
             ├─ 6046 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
             ├─25420 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
             ├─25424 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
             ├─25428 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
             ├─25430 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
             ├─25528 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
             └─25532 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf

Jul 13 00:46:58 server vsftpd[25509]: pam_pwdfile(vsftpd:auth): username is <omitted>
Jul 13 00:46:58 server vsftpd[25509]: pam_pwdfile(vsftpd:auth): got crypted password == '<omitted>'
Jul 13 00:46:58 server vsftpd[25509]: pam_pwdfile(vsftpd:auth): passwords match
```

## Some Errors

### Sample Output
```bash
vsftpd.service - vsftpd FTP server
     Loaded: loaded (/lib/systemd/system/vsftpd.service; enabled; vendor preset: enabled)
     Active: failed (Result: exit-code) since Mon 2021-07-12 12:27:04 AWST; 1min 35s ago
    Process: 155542 ExecStartPre=/bin/mkdir -p /var/run/vsftpd/empty (code=exited, status=0/SUCCESS)
    Process: 155544 ExecStart=/usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf (code=exited, status=2)
   Main PID: 155544 (code=exited, status=2)

Jul 12 12:27:04 server systemd[1]: Starting vsftpd FTP server...
Jul 12 12:27:04 server systemd[1]: Started vsftpd FTP server.
Jul 12 12:27:04 server systemd[1]: vsftpd.service: Main process exited, code=exited, status=2/INVALIDARGUMENT
Jul 12 12:27:04 server systemd[1]: vsftpd.service: Failed with result 'exit-code'.


Jul 12 12:31:11 server vsftpd[155725]: pam_unix(vsftpd:auth): authentication failure; logname= uid=0 euid=0 tty=ftp ruser=global >
Jul 12 12:31:26 server vsftpd[155725]: PAM unable to dlopen(pam_pwdfile.so): /lib/security/pam_pwdfile.so: cannot open shared obj>
Jul 12 12:31:26 server vsftpd[155725]: PAM adding faulty module: pam_pwdfile.so
Jul 12 12:31:26 server vsftpd[155725]: pam_unix(vsftpd:auth): Couldn't open /etc/securetty: No such file or directory
Jul 12 12:31:26 server vsftpd[155725]: pam_unix(vsftpd:auth): check pass; user unknown
Jul 12 12:31:26 server vsftpd[155725]: pam_unix(vsftpd:auth): authentication failure; logname= uid=0 euid=0 tty=ftp ruser=global >
Jul 12 12:31:58 server vsftpd[155725]: PAM unable to dlopen(pam_pwdfile.so): /lib/security/pam_pwdfile.so: cannot open shared obj>
Jul 12 12:31:58 server vsftpd[155725]: PAM adding faulty module: pam_pwdfile.so
Jul 12 12:31:58 server vsftpd[155725]: pam_unix(vsftpd:auth): Couldn't open /etc/securetty: No such file or directory
Jul 12 12:31:58 server vsftpd[155725]: pam_unix(vsftpd:auth): Couldn't open /etc/securetty: No such file or directory
```

### PAM adding faulty module: pam_pwdfile.so
- Solution: sudo apt-get install libpam-pwdfile

### Couldn’t open /etc/securetty: No such file or directory
- Solution: cp /usr/share/doc/util-linux/examples/securetty /etc/securetty

### 500 OOPS: vsftpd: refusing to run with writable root inside chroot()
- Reason: This is caused by the fact that the directory of the user you’re connecting to, is write-enabled. In normal chroot() situations, the parent directory needs to be read-only.

- Solution: Add this to configuration: allow_writeable_chroot=YES

## Some Management Tasks
### Generate many accounts with random passwords
- Generate random password: python3 PasswordGenerator.py (this script is under Programming/Python/Sample Folder)
- Generate user:plaintextpassword: echo $username":"$passfromabovecommand
- Generate user:encryptedpassword: echo $username":"$(openssl passwd -1 $passfromabovecommand)
```bash
for i in `cat username.txt`; do pass=$(python3 PasswordGenerator.py); echo $i":"$pass >> plaintext.txt;echo $i:$(openssl passwd -1 $pass) >> encrypted.txt; ;done
```

### Generate folders for many accounts
- Copy folder of sample account to other account: sudo cp -r $sampleaccount $newaccount
- Change ownership of folder and files to vftpuser: sudo chown -R vftpuser:vftpuser $newaccount
```bash
for i in `cat username.txt`; do sudo cp -r /$path/$sampleaccount /$path/$i; sudo chown -R vftpuser:vftpuser /$path/$i;done
```
## Reference

- https://www.golinuxcloud.com/configure-ftp-server-auth-users-ad-linux/
- https://phoenixnap.com/kb/install-ftp-server-on-ubuntu-vsftpd
- https://www.youtube.com/watch?v=DAFVYbSzCMU
- https://wiki.gentoo.org/wiki/Vsftpd/AD_Authentication
- https://techexpert.tips/vsftpd/vsftpd-kerberos-authentication/
- https://warlord0blog.wordpress.com/2015/08/04/vsftpd-ldap-active-directory-and-virtual-users/
- https://www.linuxcloudvps.com/blog/setup-virtual-users-in-vsftpd/
- https://www.programmersought.com/article/30761286278/
