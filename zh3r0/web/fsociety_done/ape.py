#!/usr/bin/python3

import requests
import hashlib

baseUrl = "http://web.zh3r0.ml:8005/code/flag.php"
#hashes = 

#for x in hashes:
data = {'code':hashlib.md5(b'fsocietyislit').hexdigest()}

r = requests.post(baseUrl, data=data)

print(data)
print(r.text)

