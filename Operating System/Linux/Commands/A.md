# Asar
- An ASAR file is an archive used to package source code for an application using Electron, an open source library used to build cross-platform programs. It is saved in a format similar to .TAR archives where files contained in the archive, such as .HTML, .JS, and .CSS files, are concatenated together without using compression.

## To extract

- Install NPM: sudo apt install npm
- Install asar using npm: npm install -g asar
    - -g: install to global mode
    - default is local which is current project directory
- Extract all files: asar extract <archive.asar> <destination>
- Extract one file from archive: asar extract-file <archive> <filename>

## Resource

- https://fileinfo.com/extension/asar