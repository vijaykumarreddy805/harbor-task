# JSON Filter Task

## Objective
Read the JSON file at `/app/input.json` and filter users who are 18 years old or older.

## Instructions
1. Read the file `/app/input.json`. It contains a JSON array of user objects, each with `name` (string) and `age` (integer) fields.
2. Filter the users whose `age` is greater than or equal to 18.
3. Write the names of the filtered users to `/app/output.txt`, one name per line, in the same order they appear in the input.

## Example
If input contains:
```json
[{"name": "Alice", "age": 20}, {"name": "Bob", "age": 15}]
```
Then `/app/output.txt` should contain:
```
Alice
```
