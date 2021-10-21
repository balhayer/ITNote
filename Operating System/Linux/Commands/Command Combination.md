# Conversion of number system in Linux shell
## Using double brackets with echo, print, printf

- To Decimal
```bash
echo $((2#00000001)) = 1
echo $((16#AB)) = 171
echo $((8#70) = 56
print $((8#70))
printf “%d\n” $((8#70)). %d = decimal
```

## Using obase,ibase and bc
```bash
Character in hex must be uppercase
echo “obase=10; ibase=16; AB” | bc
echo “obase=2; ibase=16; F” | bc
```

# Compare files
## Comm

- comm file1 file2
    - First column: Line not present in file1
    - Second column: line not present in file2
    - Third column: file present in both

## Diff

- diff file1 file2 [-u | -c]: unified or context format
    - -: line appears in first file only
    - +: line appears in second file only

## Vimdiff

- open multiple files in multiple vim windows
- do: gets changes from the other window into the current one
- dp: puts the changes from the current window into the other one
- ]c: jumps to the next change
- [c: jumps to the previous change
- C w: switches to the other split window.