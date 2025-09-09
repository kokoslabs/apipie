#you can also run python3 -m apipie config.json False, and same with the string

from apipie import Apipie

apipie=Apipie('examples/api_config.json', False)
# or
apipie=Apipie('''{
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

    "open-vars": {
        "usrnm": "kokos-lab",
        "api_key_github": "ghp_123456789",
        "api_key_weather": "abc_openweather_456"
    },

    "keys": {
        "api_key_github": "ghp_123456789",
        "api_key_weather": "abc_openweather_456"},

    "routes": {
        "hia": "httpbin",
        "aloha": "weather",
        "get/v2/run": "github",
        "test/<varname>/hia": "hia"
    },
    
    "apis": {
        "httpbin": {
            "cors": "True",
            "method": "POST",
            "url": "https://httpbin.org/post",
            "bearer_token": "<api_key_github>",
            "json": {
                "message": "Hello from <usrnm>"
            },
            "headers": {
                "X-Custom": "Header for <usrnm>"
            }
        },
        "weather": {
            "cors": "False",
            "method": "GET",
            "url": "https://api.openweathermap.org/data/2.5/weather?q=<city>&appid=[api_key_weather]"
        },
        "github": {
            "cors": "True",
            "method": "GET",
            "url": "https://api.github.com/users/<usrnm>"
        },
        "hia": {
            "cors": "False",
            "method": "GET",
            "url": "https://api.github.com/users/<varname>"
        }
    }
}''', True)

if __name__ = "__main__":
    apipie.run()
