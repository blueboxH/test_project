import requests
import json

headers = {'content-type': 'application/json'}

data = {
    "method": "foobar",
    "params": {"foo": 1, "bar": 2},
    "jsonrpc": "2.0",
    "id": 0,
}

resp = requests.post('http://localhost:4000/jsonrpc', data=json.dumps(data))

print(resp.json())

