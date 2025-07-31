***variables***

there are two kinds of variables, preset ones, and path based ones

***pre defined***

pre defined variables is a variable that is set when the code is executed and is often not edited

```json
{
    "open-vars":{
        "city": "toronto"
    },
...
```

variables are easy to use time savers

like api keys, they can be placed almost anywhere easily, but use angle braces ( < and > ) instead of square braces ( [ and ] ), example

```json
{
    "apis":{
        "get_api":{
            "method": "get",
            "url": "https://httpbin.org/get?<city>",
            "rate_limit": { "limit": 3, "window": 30 }
        }
    }
}
```

easy as that

```json
{
    "routes":{
        "get":"get_api"
    },
    "keys":{
        "api_key_identifier":"you_api_key_here"
    },
    "open-vars":{
        "city": "toronto"
    },
    "apis":{
        "get_api":{
            "method": "get",
            "url": "https://httpbin.org/get?<city>&api-key=[api_key_identifier]",
            "rate_limit": { "limit": 3, "window": 30 }
        }
    }
}
```

now lets do path based variables

they are super easy, just put the variable into the routes path
```json
{
    "routes":{
        "city/<city>":"some_nickname"
    },
...
```

and that is it, the syntax on everything else is the same

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
            "url": "https://httpbin.org/get?<city>&api-key=[api_key_identifier]",
            "rate_limit": { "limit": 3, "window": 30 }
        }
    }
}
```
now if you go to https://localhost:8000/city/toronto you should get
```json
{
    "args": {
    "api-key": "you_api_key_here", 
    "toronto": ""
  },  
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Host": "httpbin.org", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "none", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-6______4-________________"
  }, 
  "origin": "--.---.--.---", 
  "url": "https://httpbin.org/get"
}
```
