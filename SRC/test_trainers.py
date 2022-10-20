from fastapi.testclient import TestClient
from server import app
from fastapi import status

client = TestClient(app)


def test_trainers_by_pokemon():
    response = client.get("/trainers?pokemon_name=charmander")
    response_body = response.json()["trainers"]
    trainers_list = [trainer["trainer_name"]
                     for trainer in response_body]
    assert response.status_code == status.HTTP_200_OK, " status code in trainers by pokemon isn't 200"
    assert "Giovanni" in trainers_list, "Giovanni isn't in the trainers list"
    assert "Jasmine" in trainers_list, "Jasmine isn't in the trainers list"
    assert "Whitney" in trainers_list, "Whitney isn't in the trainers list"
