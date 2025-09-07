***Scripting***

Adding scripts to apipie for request and data manipulation and is super easy.

Start with a basic apipie config.json example.

```json
        "hia": {
            "require_api_key": false,
            "script": "hia",
            "cors": "False",
            "method": "GET",
            "url": "https://api.github.com/users/<varname>"
        }
```
Script has the name hia for referencing

now that the script has been defined lets get coding
lets start with something easy, how about a calculator script
to start, add the decorator in your apipie instance.
```python
from apipie import Apipie

apipie = Apipie("api_config.json", is_string=False)

@apipie.script('hia')
def calculator(request):
    pass
```

Now to add the logic use `request.args.get("some_value_here")`, and do that twice.

And to return custom type (i.e. html, json, or text, use apipie.response.json)

```python
@apipie.script('hia')
def calculator(request):
    return apipie.response.json({"result": int(request.args.get("a",1))+int(request.args.get("b",2))})
```

It is that easy, all of the data available from request variables inside a function, most of the functions available are found at flask [here](https://flask.palletsprojects.com/).

>note: this app is built off of sanic, which is Flask but faster


It is easy to change predefined or path variables at runtime using api scripting

```python

@apipie.script('somescriptnamehere')
def calculator(request):
    hia=apipie["somevariablename"]
    apipie["varname"]=hia
```