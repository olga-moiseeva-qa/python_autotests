import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '38f7ca1b417104f8c06ed1d4b2fa76fb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
trainer_id = '5293'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_responce():
    response_get = requests.get(url= f'{URL}/trainers', params={'trainer_id' : trainer_id} )
    assert response_get.json()["data"][0]["trainer_name"] == 'Хельга'

