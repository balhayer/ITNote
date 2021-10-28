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


# AWK
## Arithmetic Expressions

Operator|	Type|	Meaning|	Examples
---|---|---|---
|+ |	Arithmetic|	Addition|	7 + 3 = 10
|– |	Arithmetic|	Subtraction	|7 – 3 = 4
|* |	Arithmetic|	Multiplication |	7 * 3 = 21
|/ |	Arithmetic|	Division |	7 / 3 = 2.33333
|% |	Arithmetic|	Modulo |	7 % 3 = 1
|<space>|	String|	Concatenation|	7 3 = 73

## Autoincrement and autodecrement operators

- x++
- –y

## Assignment Operators

Operator|	Meaning
-|-
+=|Add result to variable
-=|Subtract result from variable
*=|Multiply variable by result
/=|Divide variable by result
%=|Apply modulo to variable

## Conditional expressions

Operator|	Meaning
|--|--
|==|Is equal
|!=|Is not equal to
|>|Is greater than
|>=|Is greater than or equal to
|<|Is less than
|<=|Is less than or equal to

- These operators can be used to compare numbers or strings
- With strings, lower case letters are greater than upper case letters
- A value of 0 is false, anything else is true
- Undefined variables has the value of 0

## Regular Expressions

Operator|	Meaning	Examples
--|--
~|	Matches	number ~ /(one|two|three)/
!~|	Doesn’t match	word !~ /hello/

## Sample Scripts

- Extract lines and sublines
```bash
samplerule.csv
number, name
99, Some keyword
100, ABC <some words>
100.1, ABC
100.2, <some words>
101, DEF <some words>


AWK Script
awk -F";" -v parentrule="" 'BEGIN{print "===START==="}; $2 ~ /ABC/ || $1 ~ parentrule {split($1,array,".");parentrule=array[1]; print $0;}; END{ print "\n===END===\n";}' samplerule.csv

Explanation
-F";": Field separator
-v parentrule="": assign variable
$2: column 2
$1: column 1
split($1,array,"."): split column one based on ., assign to array
```

## Reference:

https://likegeeks.com/awk-command/
https://www.grymoire.com/Unix/Awk.html