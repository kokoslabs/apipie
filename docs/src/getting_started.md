to get started, download apipie somehow

***installing apipie***

install it by running
```bash
pip install apipie
```

if you would prefer not to use a venv run 

```bash
python3 -m pip install apipie
```

or, on windows

```bash
py -m pip install apipie
```

to use you can run

```bash
apipie config.json False
```

the first argument is the filename, or the json iteself, if you would rather just input it right into there, make the second value true, that tells the code you want to use a string not a file path

you can also run it inside a .py file

example.py
```python
from apipie import main

main('config.json', False)

#or

main('{"some":{"json":"here"}}',True)
```