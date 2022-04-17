# join

## Simple implementation of nested loop join operation, which enables to join two tables in `O(n·k)` time complexity.

Script will work properly with python in version >= 3.7, because of [dictionary keys order](https://mail.python.org/pipermail/python-dev/2017-December/151283.html) assumption, which is used in this implementation.

### How to use?

If you have two `*.csv` files, e.g.

id | first_name
- | -
1 | Alice
2 | Bob
3 | Emma

and

id | surname
- | -
2 | JOHNSON
4 | BROWN
1 | SMITH

you can execute
```bash
python3 path/to/this/directory/main.py file_path file_path column_name [inner|left|right]
```
command to get output:

id | first_name | surname
- | - | -
1 | Alice | SMITH
2 | Bob | JOHNSON

Alternatively you can add alias `join` to your terminal, by running
```
echo "\nalias join='python3 path/to/this/directory/main.py'" >> .zshrc
```
After reload, you can run simply:
```
join file_path file_path column_name [inner|left|right]
```
