***services api keys and rate limiting***

you want to use a service that requires an api key, but can't expose it to the public (for obvious reasons) but want too, well here is the right place to go

>

***api keys***

it is really easy to add api keys to your apipie instance first define the api keys using the "keys" key

```json
{
    "keys":{
        "api_key_identifier":"you_api_key_here"
    },

```

it is really easy to add them to your url or whatever else

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

works with post in the same why, you can do that with headers and all that, but we will cover post later

***rate limits***

rate limits have two arguments, first is how many requests, second is the period of time between each refresh

```json
{
"rate_limit": {
     "limit": 3, 
     "window": 30 
     }
}
```

that code there has the rate limits set to 3 requests every half a minute, than it refreshes

example
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
