## CSV File/Data

### Sample CSV File: link.txt
```python
Name,URL
Cisco,http://cisco.com
Facebook,http://facebook.com
```

### Read file using csv reader
```python
import csv
file = open(“link.txt”,”rt”)
reader = csv.reader(file)
#Next(reader) # this is equal to if rownum!=0 below
rownum = 0
for row in reader:
    # Save header row.
    if rownum !=0:
        print (“{0}: {1}”.format(row[0], row[1]))
    rownum+=1
file.close()
```

### Another example for reading csv file:
```python
#!/usr/bin/python

import csv

fileaplist = open(“aplist”,”r”)
reader=csv.reader(fileaplist)
for i in reader:
    print i
fileaplist.close()
with open(“joinap”,”r”) as file:
    joinap = csv.reader(file)
    for i in joinap:
        print i
```

### Read file using csv DictReader
```python
import csv

file = open(“link.txt”,”rt”)
reader = csv.DictReader(file)
for row in reader:
    print (“{0}: {1}”.format(row[“Name”], row[“URL”]))
file.close()
```

### Write file using CSV Reader
```python
import csv

def csv_append(data, path):
“””
Append single line to a CSV file path
“””
with open(path, “at”) as file:
    writer = csv.writer(file, delimiter=’,’)
    writer.writerow(data)

def csv_writer(data, path):

“””
Write the whole data nested list to a CSV file path
“””
with open(path, “wt”) as file:
    writer = csv.writer(file, delimiter=’,’)
    for line in data:
        writer.writerow(line)

if __name__ == “__main__”:
“””
data = [“first_name,last_name,city”.split(“,”),
“Tyrese,Hirthe,Strackeport”.split(“,”),
“Jules,Dicki,Lake Nickolasville”.split(“,”),
“Dedric,Medhurst,Stiedemannberg”.split(“,”)]
“””

data=[“”,””]
data[0] = input(“Name: “)
data[1] = input(“URL: “)
path = “link.txt”
csv_append(data, path)
```

## PDF Files

### Installation
- Pymupdf: pip3 install pymupdf
- PDFMinder: pip3 install pdfminer
### Usage of pymupdf
```Python
import fitz #Pymupdf
    with fitz.open("2020-06-04-upload.pdf") as p:
        text=""
        for page in p:
            text+=page.get_text()
print(text)
```

### Usage of pdfminer
```python
from pdfminer.high_level import extract_text

pdffile = 'filename.pdf'

text = extract_text(pdffile)
print (text)
```

# Reference

- [Read and Write CSV Files in Python](https://www.learnbyexample.org/reading-and-writing-csv-files-in-python/)
- 