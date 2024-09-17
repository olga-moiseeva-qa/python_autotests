import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '38f7ca1b417104f8c06ed1d4b2fa76fb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}




response_create = requests.post(url= f'{URL}/pokemons' , headers= HEADER, json = body_create)

print(response_create.text)

message = response_create.json()['id']
print(message)

body_change = {
    "pokemon_id": message,
    "name": "Дракоша",
    "photo_id": 2
}
response_change = requests.put(url= f'{URL}/pokemons' , headers= HEADER, json = body_change)
print(response_change.text)

body_add_pokeball = {
    "pokemon_id": message
}

response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball' ,headers= HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

