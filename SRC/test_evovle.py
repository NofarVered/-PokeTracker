from ftplib import error_reply
from fastapi.testclient import TestClient
from server import app
from fastapi import status

client = TestClient(app)


def test_archie_spearow_can_not_evolve():
    response = client.put(
        "/evolve?pokemon_name=spearow&trainer_name=Archie").json()
    result = {"pokemon": "", "trainer": ""}
    assert response == result, "Archie trainer can evolve spearow even if he is not his pokemon"


def test_oddish_evolve_to_gloom():
    response = client.put(
        "/evolve?pokemon_name=oddish&trainer_name=Whitney").json()["pokemon"]
    assert response == "gloom", "oddish not evolve to gloom"
    response = client.put(
        "/evolve?pokemon_name=oddish&trainer_name=Whitney").json()["pokemon"]
    result = {"pokemon": "", "trainer": ""}
    assert response == result, "oddish is not Whitneys pokemone anymore"


def test_get_all_of_trainer_pokemons_and_see_the_evlove(self):
    response = client.get("/pokemons?trainer_name=Whitney").json()
    assert "pikachu" in response, "pikachu isn't in Whitney list"
    assert "raichu" in response, "raichu isn't in Whitney list"
    response = client.put(
        "/evolve?pokemon_name=pikachu&trainer_name=whitney").json()["pokemon"]
    assert response == "raichu", "raichu not evolve from pikachu"
