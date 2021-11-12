# VI Editor
## Configuration File:

- .vimrc in home directory
    - ai : autoindent – copy the previous line’s indentation
    - ts=2 : tabstop – set the number of spaces that the Tab key uses, when pressed
    - sw=2 : shiftwidth – number of spaces to use with autoindent
    - et : expandtab – use the space character as whitespace instead of Tab
    - cuc : cursorcolumn – highlight the column the cursor is on
    - nu: number – turn on line numbering
- Example:
```bash
§ autocmd FileType yaml setlocal ai ts=2 sw=2 et: convert tab to 2 spaces
§ autocmd FileType yaml setlocal ai ts=2 sw=2 et cuc nu: like above + highlight column and turn on line numbering
```
- Some settings:
    ○ Set showcmd
    ○ Set nocursorline
    ○ Set ignorecase
    ○ Set number|nonumber: show/Hide line number
    ○ Set relativenumber|norelativenumber
    ○ Set incsearch
    ○ Set hlsearch
    ○ Set tabstop=4
    ○ Set softtabstop=4
    ○ Set list|nolist: show line feeding
    ○ Set ff: show file format = dos/unix
    ○ Set cursorcolumn: highlight whole column of cursor
    :set all: show all options

## Commands
### Copying: Yanking
- Yanking text Like deletion, almost all yank commands are performed by typing y followed by a motion. For 

#### Example

- y$ yanks to the end of line. 
- <numbyyer>yy = <number>:y : yank number of line

### Pasting: p|P
- Putting text put after position or after line p 
- Putting before position or before line P 

### Saving
- :w: save document
- ZZ = :wq: save document and exit
- :!q: quit without saving

### Undo: u
### Redo: Ctrl_r

### Repeat previous command at current cursor: .

### Show statistics, word count
- Ctrl_g: show statistics
- g, Ctrl_g: word counts

### Running Shell command from VI: :!
- Read in output of command: :r !

### Goto:
- First line: 1,Shift_g
- Last line: shift_g
- Line number: :
- G: go to line number

### Moving around:
- H/L: Top/End of page
- 1_Shift_G/Shift_G: Top/End of document:q
- w/W: go forward word by word/the whole phrase separated by space
- Shift_f/Shift_b: Page down (forward) /Page up (backward)

### Searching:
- /
- n/N: search again next forward/backward

### Replace string:
- :s//
- :%s//: replace all lines
- :%s///g: replace all lines without asking
- :%s/\n/,/g: replace all new line with comma, make a list of item separated by comma
- :help range: get help for range 

### Indent multiple line:
- Press V to change to visual mode
- Then press j to highlight lines
- Press > to indent

### Inserting text 
- before cursor, before line i , I 
- append after cursor, after line a , A 
- open new line after, line before o , O 
- replace one char, many chars r , R

### Motion 
- left, down, up, right h , j , k , l 
- next word, blank delimited word w , W 
- beginning of word, of blank delimited word b , B 
- end of word, of blank delimited word e , E 
- sentence back, forward ( , ) 
- paragraph back, forward { , } 
- beginning, end of line 0 (or ^) , $ 
- beginning, end of file 1G (or gg) , G 
- line n n G or :n 
- forward, back to char c fc , Fc 
- forward, back to before char c tc , Tc 
- top, middle, bottom of screen H , M , L

### Deleting text 
- Almost all deletion commands are performed by typing d followed by a motion. 
- For example 
    - dw deletes a word. 
    - A few other deletions are: character to right, left x , X 
    - to end of line D line 
    - dd line :d

Changing text The change command is a deletion command that leaves the editor in insert mode. It is performed by typing c followed by a motion. For example cw changes a word. A few other change commands are: to end of line C line cc

Registers Named registers may be specified before any deletion, change, yank, or put command. The general prefix has the form “c where c may be any lower case letter. For example, “adw deletes a word into register a. It may thereafter be put back into the text with an appropriate put command, for example “ap.

Markers Named markers may be set on any line of a file. Any lower case letter may be a marker name. Markers may also be used as the limits for ranges. set marker c on this line mc goto marker c ‘c goto marker c first non-blank ’c

Search for strings search forward /string search backward ?string repeat search in same, reverse direction n , N

Replace The search and replace function is accomplished with the :s command. It is commonly used in combination with ranges or the :g command (below). replace pattern with string :s/pattern /string /flags flags: all on each line, confirm each g , c repeat last :s command &

Regular expressions any single character except newline . (dot) zero or more repeats * any character in set […] any character not in set [^ …] beginning, end of line ^ , $ beginning, end of word \< , > grouping (. . . ) contents of n th grouping \n

Counts Nearly every command may be preceded by a number that specifies how many times it is to be performed. For example 5dw will delete 5 words and 3fe will move the cursor forward to the 3rd occurance of the letter e. Even insertions may be repeated conveniently with this method, say to insert the same line 100 times.

Ranges Ranges may precede most “colon” commands and cause them to be executed on a line or lines. For example :3,7d would delete lines 3−7. Ranges are commonly combined with the :s command to perform a replacement on several lines, as with :.,$s/pattern/string/g to make a replacement from the current line to the end of the file. lines n-m :n ,m current line :. last line :$ marker c :’c all lines :% all matching lines :g/pattern /

Files write file (current file if no name given) :w file append file (current file if no name given) :w >>file read file after line :r file read program output :r !program next file :n previous file :prev edit new file :e file replace line with program output :.!program

Other toggle upper/lower case ~ join lines J repeat last text-changing command . undo last change, all changes on line u , U

## Reference

- https://linuxacademy.com/blog/linux/vi-short-cuts-for-beginners/
- https://mediatemple.net/community/products/dv/204644480/enabling-vi-syntax-colors
- Talk on going mouseless with Vim, Tmux, and Hotkeys: https://www.youtube.com/watch?v=E-ZbrtoSuzw
- Mastering the Vim Language: https://www.youtube.com/watch?v=wlR5gYd6um0