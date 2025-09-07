***Services API keys and rate limiting***

You want to use a service that requires an api key, but can't expose it to the public (for obvious reasons) but want too, well here is the right place to go.

>

***Api keys***

It is really easy to add api keys to your apipie instance first define the api keys using the "keys" key.

```json
{
    "keys":{
        "api_key_identifier":"you_api_key_here"
    },

```

It is really easy to add them to your url or whatever else.

```json

{
    "routes":{
        "get":"get_api"
    },
    "keys":{
        "api_key_identifier":"you_api_key_here"
    },
    "apis":{
        "get_api":{
            "method": "get",
            "url": "https://httpbin.org/get?api-key=[api_key_identifier]"
        }
    }
}
```

Works with post in the same why, you can do that with headers and all that, but we will cover post later.

***rate limits***

Rate limits have two arguments, first is how many requests, second is the period of time between each refresh.

```json
{
    "rate_limit": {
         "limit": 3, 
        "window": 30 
    }
}
```

That code there has the rate limits set to 3 requests every half a minute, than it refreshes.

Example
```json

{
    "routes":{
        "get":"get_api"
    },
    "keys":{
        "api_key_identifier":"you_api_key_here"
    },
    "apis":{
        "get_api":{
            "method": "get",
            "url": "https://httpbin.org/get?api-key=[api_key_identifier]",
            "rate_limit": { "limit": 3, "window": 30 }
        }
    }
}
```
