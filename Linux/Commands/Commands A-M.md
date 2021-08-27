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

## Find text in all file
    - grep -rnw ./ -e 'expression': search all files recursively for expression whole word, show file number
    - grep --include=\*.{c,h} -rnw '/path/to/somewhere/' -e "pattern": only search file with .c or .h
    - grep --exclude=\*.o -rnw '/path/to/somewhere/' -e "pattern": don't search file .o
    - grep --exclude-dir={dir1,dir2,*.dst} -rnw '/path/to/somewhere/' -e "pattern": exclude some directory
	-   Grep “text” file.txt
	-   Grep -n “text” file.txt: print line number with output
	-   Grep -i “text” file.txt: -i case insensitive
	-   Grep -vi “text” file.txt: -v omit line with text
	-   Grep -E “[hijk]” file.txt: -E Extended regular expression
	-   Grep -G “[hijk]” file.txt: -G Standard regular expression
	-   Grep -oP “\d{1,5}/open” file.txt: -o show only matching part, -P Perl regular expression
	-   Grep -E “\w{6,}” file.txt: word longer than 6 characters
	-   Grep –color=auto “text” text.txt
	-   Export GREP_OPTIONS=’–color=auto’
	-   Grep -I break-in auth.log | awk {‘print $12’}
	-   Search for file with specific string: grep -il “ip policy route-map zScaler-Tunnel” ./*.*
		-   i: ignore case
		-   l: list filename (remove this to show search string after each file)
	-   Grep ‘text1\|text2’ filename: Grep or
	-   Grep -E ‘text1|text2’ filename: grep or
	-   Egrep ‘text1|text2’ filename: grep or
	-   Grep -e ‘text1’ -e ‘text2’ filenameA
	-   grep -E ‘pattern1.*pattern2’ filename: grep and
	-   grep -E ‘pattern1.*pattern2|pattern2.*pattern1’ filename: grep and
	-   grep -E ‘pattern1’ filename | grep -E ‘pattern2’: grep and
	-   grep -B2 -A2 -a ‘[a-z0-9]\{32\}’ /dev/sdb: 2 line before (B2) and 2 line after (A2), treat binary as text (-a), 32 characters of (a-z0-9)
	-   grep -oP ‘d{1,5}/open’ file: search for digit length from 1 to 5/open (PERL regex -P), show only matching (-o)
	-   Grep -rnwl <path> -e “text”: search for file with specific text
		-   r: recursive
		-   n: line number
		-   w: match whole word
		-   l: list file name of matching files
		-   i: ignore case
		-   Using find: find /usr/share/wordlists/* -name ‘*’ -exec grep -il ‘eliot’ {} \; -print

## Reference
-   [https://www.thegeekstuff.com/2011/10/grep-or-and-not-operators](https://www.thegeekstuff.com/2011/10/grep-or-and-not-operators)
-   [https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux#regular-expressions](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux#regular-expressions)
-   [https://www.cyberciti.biz/faq/grep-regular-expressions/](https://www.cyberciti.biz/faq/grep-regular-expressions/)
-   [https://opensourceforu.com/2012/06/beginners-guide-gnu-grep-basics/?utm_source=pushengage&utm_medium=pushnotification&utm_campaign=pushengage](https://opensourceforu.com/2012/06/beginners-guide-gnu-grep-basics/?utm_source=pushengage&utm_medium=pushnotification&utm_campaign=pushengage)