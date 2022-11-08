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


def test_get_types_of_pokemon_dup():
    response = client.get("/pokemons/eevee")
    response_body = response.json()["types"]
    assert response.status_code == status.HTTP_200_OK, " status code in get types of pokemon isn't 200"
    assert len(response_body) == len(set(response_body)
                                     ), "one of the elements appears twice in the list"


def test_pokemon_types_updated():
    response = client.get("/pokemons/venusaur")
    response_body = response.json()["types"]
    assert response.status_code == status.HTTP_200_OK, " status code in pokemon types updated isn't 200"
    assert "grass" in response_body, "grass isn't int the types list "
    assert "poison" in response_body, "poison isn't int the types list "


def test_delete_pokemon_of_trainer():
    first_response = client.get("/pokemons?trainer_name=Whitney")
    assert first_response.status_code == status.HTTP_200_OK, " status code in get pokemons by trainer isn't 200"
    first_response_body = first_response.json()["pokemons"]
    assert "vileplume" in [pokemon["pokemon_name"]
                           for pokemon in first_response_body], "vileplume isn't in the pokemons list"
    second_response = client.delete(
        "/trainers?pokemon_name=vileplume&trainer_name=Whitney")
    assert second_response.status_code == status.HTTP_204_NO_CONTENT, " status code in delete pokemon of_trainer isn't 204"
    third_response = client.get("/pokemons?trainer_name=Whitney")
    third_response_body = third_response.json()["pokemons"]
    assert "vileplume" not in [pokemon["pokemon_name"]
                               for pokemon in third_response_body], "vileplume is in the pokemons list"


def test_get_pokemons_by_owner():
    response = client.get("/pokemons?trainer_name=Drasna")
    response_body = response.json()["pokemons"]
    assert response.status_code == status.HTTP_200_OK, " status code in get pokemon by type isn't 200"
    assert "wartortle" in [pokemon["pokemon_name"]
                           for pokemon in response_body], "wartortle isn't in the list"
    assert "beedrill" in [pokemon["pokemon_name"]
                          for pokemon in response_body], "beedrill isn't in the list"
