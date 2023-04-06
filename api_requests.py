import requests
import json

# GET
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se184ew")
print(post_codes_req)
print(post_codes_req.status_code)
# print(post_codes_req.headers)
print(post_codes_req.content)
print(post_codes_req.json())
print(type(post_codes_req.content))
print(type(post_codes_req.json()))

pokemon_req = requests.get("https://p)

# POST - Very API dependent.
# json.dumps() - Turns a python object into a JSON string (converts)
json_body = json.dumps({"postcodes": ["PR* 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}
post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)
print(post_multi_req.json())

pokemon