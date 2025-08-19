from sanic import Sanic, response, Blueprint
from sanic.exceptions import Forbidden, SanicException
from sanic.response import html
from requests import request
from time import time
from .rate_limit import rate_limit
from .call import call_api
#from pieworker import connect #.mainTomoduleConnector
import json
import hashlib
import sys, os

#connect = connect.mainToModuleConnector

os.environ['SOMETHING'] = 'somevalue'

def import_from_path(name, path):
    import importlib.util, sys, os
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from path: {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def execute(exec_code: str):
    if exec_code.lower().startswith("file:"):
        file_path = exec_code.split("file:")[1].strip()
        mod = import_from_path("script_file", file_path)
        # Only call main() if you're sure it should
        if hasattr(mod, "main"):
            mod.main()


    elif exec_code.lower().startswith("function:"):
        func_info = exec_code.split("function:")[1].strip()
        path, func = func_info.split(">")
        path = path.strip()
        func = func.strip()

        # Load the module
        mod = import_from_path("script_func", path)

        # Run the function if it exists
        if hasattr(mod, func):
            getattr(mod, func)()
        else:
            print(f"Function `{func}` not found in {path}.")

    else:
        # Direct Python code
        exec(exec_code)

class verification:    
    def hash_api_key(key: str) -> str:
        return hashlib.sha256(key.encode('utf-8')).hexdigest()

    def get_user_by_api_key(provided_key: str, users: dict) -> tuple:
        provided_key_hash = verification.hash_api_key(provided_key)
        for username, data in users.items():
            if data.get("api_key_hash") == provided_key_hash:
                return username, data
        return None, None

def main(config_path: str, is_string: bool = False):
    print(config_path)
    def replace_keys(_str, _keys):
        for k, v in _keys.items():
            replaced = _str.replace(f'[{k}]', v)
            print(f"Replaced [{k}] with {v} in config_str")
            
        for k, v in os.environ.items():
            if  k in replaced:
                replaced = replaced.replace(f'{{{k}}}', v)
                print(f"Replaced {{{k}}} with {v} in config_str")
        print("Final replaced config_str:", replaced)
        return replaced
    
    app = Sanic("API_Proxy")
    bp = Blueprint("proxy_routes")

    if is_string:
        config = config_path
    else:
        path = config_path.strip('\'"')  # Remove single or double quotes
        with open(path) as f:
            config = f.read()
            
    print(config)

    foo = json.loads(config)
    keys = foo["keys"]
    replaced = replace_keys(config, keys)
    config = json.loads(replaced)
    users = config["users"]
    othervars = config.get("open-vars", {})
    routes = list(config["routes"].keys())
    route_to_api_key = config["routes"]
    apis = config["apis"]
    keys = config["keys"]

    def make_handler(api_name, api_config):
        cors_enabled = str(api_config.get("cors", "False")).lower() == "true"
        require_api_key = api_config.get("require_api_key", True)
        rate_limit_cfg = api_config.get("rate_limit", {"limit": 5, "window": 60})
        #script = api_config.get("script", None) #coming soon
        #print(script, api_name, api_config)

        async def handler(request, **path_vars):
            # 1. Optionally check API Key authorization
            api_key = request.headers.get("X-API-Key") or request.args.get("api_key")
            username, user_data = None, None
            if require_api_key:
                if not api_key:
                    raise Forbidden("Missing API Key")
                username, user_data = verification.get_user_by_api_key(api_key, users)
                if not user_data:
                    raise Forbidden("Invalid API Key")
                if api_name not in user_data.get("allowed_apis", []):
                    raise Forbidden("API access denied for this key")
                
            output, script_vars = None
            connection=hashlib.sha256(api_name+api_config+apis.encode('utf-8')).hexdigest()
            connect.createConnection(connection)
            connect.addData(connection,str(othervars)+'|'+str(path_vars))
            
            '''if script:
                result = execute(script)''' # coming soon

            merged_vars = {
                **othervars,
                **{k: v for k, v in request.args.items()},
                **{k: v[0] if isinstance(v, list) else v for k, v in request.form.items()},
                **path_vars
                #**script_vars
            }
            print("Merged vars:", merged_vars)
            '''output = None
            if script:
                result = execute(script)''' #coming soon
            #print(output)
            result = call_api(api_config, merged_vars)
            try:
                resp = response.text(result.text)
            except Exception:
                resp = response.text(str(result))

            if cors_enabled:
                resp.headers["Access-Control-Allow-Origin"] = "*"
                resp.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, OPTIONS"
                resp.headers["Access-Control-Allow-Headers"] = "*"
            return resp

        # Per-API rate limiting
        limit = int(rate_limit_cfg.get("limit", 5))
        window = int(rate_limit_cfg.get("window", 60))
        handler = rate_limit(limit, window, scope="ip")(handler)

        return handler

    for route in routes:
        api_key = route_to_api_key[route]
        config_entry = apis[api_key]
        method = config_entry.get("method", "GET").upper()
        handler = make_handler(api_key, config_entry)
        app.add_route(handler, f"/{route}", methods=[method, "OPTIONS"], name=f"handler_{route}")

    @bp.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
    async def proxy(request, path):
        api_key = request.args.get("api_key") or request.headers.get("X-API-Key")
        if not api_key or not is_valid_key(api_key):
            return response.json({"error": "Invalid API Key"}, status=401)
    
    app.run(host="127.0.0.1", port=8000, debug=True, single_process=True)
    
if __name__ == "__main__":
    import sys
    main(
        config_path=sys.argv[1] if len(sys.argv) > 1 else 'api_config.json',
        is_string=(sys.argv[2].lower() == 'true') if len(sys.argv) > 2 else False
    )
