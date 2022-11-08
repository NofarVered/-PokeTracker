from ftplib import error_reply
from fastapi.testclient import TestClient
from server import app
from fastapi import status

client = TestClient(app)


def test_pinsir_pokemon_can_not_evolve():
    response = client.put(
        "/evolve?pokemon_name=pinsir&trainer_name=Drake").json()
    result = {
        "pokemon": "",
        "trainer": ""
    }
    assert response == result, "pinsir pokemon can evolve"


def test_oddish_should_evolve_to_gloom():
    response = client.put(
        "/evolve?pokemon_name=oddish&trainer_name=Whitney").json()
    result = {
        "pokemon": "gloom",
        "trainer": "Whitney"
    }
    assert response == result, "Whitney's oddish not evolve to gloom"


# def test_trainer_should_not_have_the_prevuos_pokemon():
#     response = client.put(
#         "/evolve?pokemon_name=oddish&trainer_name=Whitney").json()
#     result = {
#         "pokemon": "gloom",
#         "trainer": "Whitney"
#     }
#     assert response == result, "Whitney's oddish not evolve to gloom"
#     response = client.get(
#         "/pokemons?trainer_name=Whitney").json()["pokemons"]
#     trainerPokemonsList = [pokemon["pokemon_name"]
#                            for pokemon in response]
#     assert "oddish" not in trainerPokemonsList, "oddish is still in Whitney's list"


def test_get_all_of_trainer_pokemons_and_see_the_evlove():
    response = client.get(
        "/pokemons?trainer_name=Whitney").json()["pokemons"]
    trainerPokemonsList = [pokemon["pokemon_name"]
                           for pokemon in response]
    assert "pikachu" in trainerPokemonsList, "pikachu isn't in Whitney list"
    assert "raichu" in trainerPokemonsList, "raichu isn't in Whitney list"
    response = client.put(
        "/evolve?pokemon_name=pikachu&trainer_name=whitney").json()
    result = {
        "pokemon": "raichu",
        "trainer": "whitney"
    }
    assert response == result, "raichu not evolve from pikachu"
