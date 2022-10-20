from unicodedata import name
from fastapi.testclient import TestClient
from server import app
from fastapi import status

client = TestClient(app)


def test_get_pokemon_by_type():
    response = client.get("/pokemons?pokemon_type=normal")
    response_body = response.json()["pokemons"]
    assert response.status_code == status.HTTP_200_OK, " status code in get pokemon by type isn't 200"
    assert "eevee" in [pokemon["name"]
                       for pokemon in response_body], "eevee isn't in the list"
