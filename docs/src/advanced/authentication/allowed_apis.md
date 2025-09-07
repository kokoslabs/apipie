**Allowed APIs**

you may not always want all you apis to be open, or authenticated with all api users, you can set multiple users, multiple apis, multiple allowed apis, etc

```json

{"allowed_apis":["multiple","api","names","here"]}

```

full example

```json
{
    "users": {
        "user1": {
            "api_key_hash": "912f3c265c1876046e0f147413cc1189e28af1e8c1ebbad5c485b71cd8027840",
            "allowed_apis": ["httpbin", "github"],
            "rate_limit": {"limit": 5, "window": 60}
        },
        "user2": {
            "api_key_hash": "6f8705b12a8f69fd97cb0a3df5862b35be54161b7df8f5df0e8db1e2d7b317a3",
            "allowed_apis": ["weather","hia"],
            "rate_limit": {"limit": 3, "window": 30}
        }
    },
```

*note*: the keys for each one is 35b1b4d5fdcccb5b7d1a7d7870f647002b370b18bc3d5f0b552c011ff07b0d9c and 33f63ece2c910df2959e0a870f9ef83cbdc09b1b6678d037a12c17ab5fedc51d