***apis and nicknames***


lets start with code that sends and receives our get/post request

to start lets define our api nickname

```json
{
    "apis":{
        "get_api":{
            "method": "get",
            "url": "https://httpbin.org/get"
        }
    }
}
```

now that that is defined, you can run the code, but nothing will happen, that is because we need to define the url path. it is super simple, put this at the very beginning.

```json
{
    "routes":{
        "get":"get_api"
    },

```

full code here

```json
{
    "routes":{
        "get":"get_api"
    },

    "apis":{
        "get_api":{
            "method": "get",
            "url": "https://httpbin.org/get"
        }
    }
}
```

go to http://localhost:8000, you should get a result similar to this

```json

{
  "args": {}, 
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

if you want you can change it to a post requests, and send a post request to that address if you want
```json
{
    "routes":{
        "get":"get_api"
    },

    "apis":{
        "get_api":{
            "method": "post",
            "url": "https://httpbin.org/post"
        }
    }
}
```

multiple routes is just as easy, just define them with a nickname, than expose that route to apipie via "routes"

```json
{
    "routes":{
        "post":"post_api",
        "get":"get_api",
        "example/here":"example"
    },

    "apis":{
        "post_api":{
            "method": "post",
            "url": "https://httpbin.org/post"
        },
        "get_api":{
            "method": "get",
            "url": "https://httpbin.org/get"
        },
        "example":{
            "method": "get",
            "url":"api.example.com/enpoint"
        }
    }
}
```
