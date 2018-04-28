import requests

data = {
    'text': 'thie is the text',
    'width': 50
}

url = "http://127.0.0.1:8000/wrap"
resp = requests.post(url, data=data)
print(resp.text)
