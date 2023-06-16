import requests
import json
# get request

post_codes_req = requests.get("https://api.postcodes.io/postcodes/sl61tx")

print(post_codes_req) # <Response [200]>
print(post_codes_req.status_code) # 200
print(post_codes_req.content) # turns content from URI, as bytes
print(post_codes_req.json()) # turns content into python dict
print(type(post_codes_req.json())) # shows the type is now dict

# POST request - sending data to the API

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())

# Pokermon api

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/")
print(pokemon_req.json())

# bbc_request = requests.get("https://bbc.com/")
# print(bbc_request.content)

import requests
pokemon_req = requests.get("https://pokeapi.co/api/v2/")

print(pokemon_req)