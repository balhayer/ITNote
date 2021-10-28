# OpenSSL

## Encrypt file:

- openssl enc -e -aes256 -in file.ext -out file.ext.e

## Decrypt file:

- openssl enc -d -aes256 -in file.ext.e -out file.ext

## Options:

- enc: symmetric cipher routine
- -e: encrypt
- -d: decrypt
- -aes256: cipher
- -l: list cipher

## Encrypt and tar file

- tar czf - * | openssl enc -e -aes256 -out file.tar.gz.e

## Decrypt and untar file to folder

- openssl enc -d -aes256 -in file.tar.gz.e | tar xz -C folder


## Options of tar command:

- -: output to stdout
- -C <folder>: extract to folder
- c: create archive
- z: compress using gzip
- f: location of file/filename
- x: extract archive

## Reference:
- https://www.openssl.org/docs/man1.1.1/man1/enc.html