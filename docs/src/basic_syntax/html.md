***Custom html responses***

You don't have to be stuck with plain old api requests, why not set your own custom html requests and use html files as well.


example
```json
{
    "apis"{
        "index": {
            "require_api_key": false,
            "method":"GET",
            "html": "<h1>Welcome to Apipie API Service</h1><p>Use /api/{api_name} to access APIs.</p>"
        },
    }
}
```

And you can also use just plain old files.

index.html
```html
Hello World! this is an html file served with apipie
```

api_config.json

```json
{
    "apis"{
        "index": {
            "require_api_key": false,
            "method":"GET",
            "html_file":"index.html" 
        },
    }
}
```