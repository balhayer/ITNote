# JQ command for JSON Processing
## Installation on Ubuntu

- apt-get install jq

## Some Filter

- jq ‘.’ file.json: print whole json file as . is root
- echo ‘{“fruit”:{“name”:”apple”,”color”:”green”,”price”:1.20}}’ | jq ‘.fruit’: accessing fruit key
- echo ‘{“fruit”:{“name”:”apple”,”color”:”green”,”price”:1.20}}’ | jq ‘.fruit.name’: accessing name of fruit
- jq ‘.fruit.color,.fruit.price’ fruit.json: accessing multiple keys
- echo ‘{ “with space”: “hello” }’ | jq ‘.”with space”‘: key with space
- echo ‘[“x”,”y”,”z”]’ | jq ‘.[]’: iterate over an array
- jq ‘.[] | .name’ fruits.json or jq ‘.[].name’ fruits.json: iterate over an array and access name key of each object
- jq ‘.[1].price’ fruits.json: access 1 object in the array
- echo ‘[1,2,3,4,5,6,7,8,9,10]’ | jq ‘.[6:9]’: slicing to return subarray of an array, first index is inclusive, last index is exclusive which means from item 6-8
- echo ‘[1,2,3,4,5,6,7,8,9,10]’ | jq ‘.[:6]’: this is equal to [0:6]
- jq ‘.[-2:]’: start from 2 item from the end until the end of the array
- jq ‘.fruit | keys’ fruit.json: get keys of objects
- jq ‘.fruit | length‘ fruit.json: return length or number of properties in an object
- jq ‘.fruit.name | length‘ fruit.json: get length of string
- jq ‘map(has(“name”))‘ fruit.json: check if there’s name property
- jq ‘map(.price+2)‘ fruit.json: do operation to an elements
- jq ‘[.[].price] | min‘ fruits.json or jq ‘[.[].price] | max‘: get min|max value
- jq ‘.[] | select(.price>0.5)‘ fruits.json: select item with criteria
- jq ‘.[] | select(.color==”yellow”)‘ fruits.json
- jq ‘.[] | select(.color==”yellow” and .price>=0.5)‘ fruits.json
- jq ‘.[] | select(.name|test(“^a.”)) | .price’ fruits.json: Using regular expression to check condition: get price of all item whose name start with letter a
- jq ‘map(.color) | unique‘: find unique colors, map function create another array and pass it to unique function
- jq ‘del(.fruit.name)‘ fruits.json: delete a key and value
- jq ‘.query.pages | [.[] | map(.) | .[] | {page_title: .title, page_description: .extract}]‘ wikipedia.json: transforming from a large json data to a customized one which just get 2 properties which are title and description

## Reference
- https://www.baeldung.com/linux/jq-command-json
- https://stedolan.github.io/jq/manual/#Basicfilters