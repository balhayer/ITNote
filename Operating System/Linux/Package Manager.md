# Linux Package Manager
## Advanced Package Tool (Apt) – Ubuntu, Debian-based Distro

- apt update: update list of available packages
- apt upgrade [package name]: upgraded installed packages after database has been updated
- apt-cache search [keyword]: display information stored in cache, search in name and description
- apt show [keyword]: Show information about a package
- apt install {package name} [-y]
- apt remove [–purge]: remove package, –purge will remove all leftover configuration

## dpkg

- dpkg -i package.deb: install .deb package

## RPM - Redhat, CentOS
- rpm -qa | grep -i <$keyword>: search for package
- rpm -e <$package name>: erase/remove package
- rpm -ivh <$package.rpm>: Install package