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


def test_get_types_of_pokemon():
    response = client.get("/pokemons/eevee")
    response_body = response.json()["types"]
    assert response.status_code == status.HTTP_200_OK, " status code in get types of pokemon isn't 200"
    assert len(response_body) == len(set(response_body)
                                     ), "one of the elements appears twice in the list"
