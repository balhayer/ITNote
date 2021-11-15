# CSV File
## Read CSV Files
```nim
import parsecsv

var p: CsvParser
p.open("sample1.csv")
p.readHeaderRow()
while p.readRow():
  echo "The average of ", p.row[0], " in ", 
    p.headers[2], " is ", p.row[1]
```
## Reference

- https://titanwolf.org/Network/Articles/Article?AID=963518c2-7ab0-41e8-9f29-ca30a012797b
- https://docs.w3cub.com/nim/parsecsv
- https://tudurikata.com/post/nim-csv-en/