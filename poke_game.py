import requests
import random

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118")
data = response.json()

random_pokemon = random.choice(data["results"])
print(random_pokemon)

response1 = requests.get(random_pokemon["url"])
data1 = response1.json()
print(data1)