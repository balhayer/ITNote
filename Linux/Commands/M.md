# Mysql
## Login to mysql
```bash
mysql -u root
mysql -u root -p: login with password
```

## Use database
```bash
show databases;
user $databasename;
```

## Create and Delete user
```bash
CREATE USER ‘$user’@’$host’ IDENTIFIED BY ‘$password’;
View created users: Select user from mysql.user;
Change password: ALTER USER ‘$user’@’$host’ IDENTIFIED BY ‘$newpassword’;
DROP USER ‘$user’@’$host’
After delete user, update status: FLUSH PRIVILEGES;
```

## Grant Permission
```bash
GRANT ALL PRIVILEGES ON *.* TO ‘user1’@localhost IDENTIFIED BY ‘password1’;
GRANT ALL PRIVILEGES ON ‘yourDB’.* TO ‘user1’@localhost;
FLUSH PRIVILEGES;
SHOW GRANTS FOR ‘user1’@localhost;
```

## Create Table
```bash
CREATE TABLE $Name ( $columnname $datatype($length))
Example: CREATE TABLE Content (Output Text(4096));
```

# Reference

https://phoenixnap.com/kb/how-to-create-mariadb-user-grant-privileges