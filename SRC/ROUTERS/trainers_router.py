from fastapi import APIRouter, HTTPException, Request, status
import requests
from PokeTracker.SRC.API_DATA_RETRIEVE.my_sql_auth import my_sql_auth
from PokeTracker.SRC.API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from PokeTracker.SRC.API_DATA_RETRIEVE.utils.querys import *
from PokeTracker.SRC.CREATE_DB_SCRIPT.queries.insert_querys import INSERT_INTO_TRAINERS_INFO
from PokeTracker.SRC.CREATE_DB_SCRIPT.services.id_manager import Id_manager

AUTH = my_sql_auth()
CONNECTOR = my_sql_proxy(AUTH)

router = APIRouter()


@router.get("/trainers", status_code=200)
def get_trainers_by_pokemon(pokemonName):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TRAINERS, [
            pokemonName])
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid pokemon name"
        )


@router.post("/trainers", status_code=201)
async def adding_trainer(request: Request):
    req = await request.json()
    try:
        trainer_id = Id_manager.id_encoding(req["name"], req["town"])
        CONNECTOR.execute_insert_query(INSERT_INTO_TRAINERS_INFO, [
            req["name"], req["town"], trainer_id])
        return {"name": req["name"],
                "town": req["town"], "trainer id": trainer_id}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Trainer"
        )


@router.delete("/trainers/", status_code=204)
def remove_pokemon_of_trainer(pokemon_name: str, trainerName: str):
    pokemon_info = CONNECTOR.execute_select_one_query(SELECT_POKEMON_BY_NAME, [
        pokemon_name])
    trainer_info = CONNECTOR.execute_select_one_query(SELECT_TRAINER_BY_NAME, [
        trainerName])
    CONNECTOR.execute_insert_query(DELETE_POKEMON_OF_TRAINER, [
        trainer_info["trainer_id"], pokemon_info["pokemon_id"]])
