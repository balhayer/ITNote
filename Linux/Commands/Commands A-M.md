# Grep

## Options:
- -i: ignore case
- -r: recursive
- -n: show line number
- -w: whole word
- -e: expression to search
- -l: filename of matching files
- --include: include criteria
- --exclude: exclude criteria
- --exclude-dir: exclude 1 or more directory
- 
## Find text in all file
    - grep -rnw ./ -e 'expression': search all files recursively for expression whole word, show file number
    - grep --include=\*.{c,h} -rnw '/path/to/somewhere/' -e "pattern": only search file with .c or .h
    - grep --exclude=\*.o -rnw '/path/to/somewhere/' -e "pattern": don't search file .o
    - grep --exclude-dir={dir1,dir2,*.dst} -rnw '/path/to/somewhere/' -e "pattern": exclude some directory