# Zip and Unzip
## Installation

- apt-get install zip

## Example of ZIP command

- zip <archive.zip> <files>: create archive from file or file list, separated by space
- zip -e <archive.zip> <files>: encrypt with a password
- zip -r <archive.zip> <files>: Zip directory including subdirectory recursively
- zip -Z bzip2 <archive.zip> <files>: specify compression method, by default method is deflate, if file can’t be compressed, store method is used
- zip -6 <archive.zip> <files>: level of compression 0-9 (no compression – most compressed), default is 6
- zip -s <size> <archive.zip> <files>: create split zip file size can be: k (kilobytes), m (megabytes), g (gigabytes), t (terabytes), e.g: 1g, 100m
- zip -d <archive.zip> <file>: delete file from archive, get list using unzip -l <archive.zip>

## Example of Unzip command

- unzip <archive.zip>: unzip archive
- unzip -l <archive.zip>: list content of archive
- unzip <archive.zip> <file>: unzip file from archive
- unzip <archive.zip> <-x file>: unzip all except file from archive