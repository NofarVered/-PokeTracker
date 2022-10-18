from fastapi import FastAPI, HTTPException, status, Request
import requests
import uvicorn
from SRC.CREATE_DB_SCRIPT.load_data import load_data
from SRC.API_DATA_RETRIEVE.my_sql_auth import my_sql_auth
from SRC.API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from SRC.API_DATA_RETRIEVE.utils.querys import *
from SRC.CREATE_DB_SCRIPT.queries.insert_querys import INSERT_INTO_TRAINERS_INFO
from SRC.CREATE_DB_SCRIPT.services.id_manager import Id_manager

app = FastAPI()
db_auto = my_sql_auth()
CONNECTOR = my_sql_proxy(db_auto)
load_data(CONNECTOR)


@app.get("/")
def root():
    return "server is running"


@app.get("/pokemons", status_code=200)
def get_pokemons_by_trainer(trainerName):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TRAINERS, [
            trainerName])
        return {"pokemons": result}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid trainer name"
        )


@app.get("/pokemons", status_code=200)
def get_pokemons_by_type(pokemonType):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TYPE, [
            pokemonType])
        return {"pokemons": result}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid pokemon type"
        )


@app.get("/pokemons/heaviest", status_code=200)
def get_pokemons_by_type():
    try:
        result = CONNECTOR.execute_select_one_query(
            SELECT_HEAVIEST_POKEMON, [])
        return {"pokemon": result}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@app.get("/pokemons/popular", status_code=200)
def get_pokemons_by_type():
    try:
        result = CONNECTOR.execute_select_one_query(
            SELECT_POPULAR_POKEMON, [])
        return {"pokemon": result}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@app.get("/trainers", status_code=200)
def get_trainers_by_pokemon(pokemonName):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TRAINERS, [
            pokemonName])
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid pokemon name"
        )


@app.post("/trainers", status_code=201)
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


@app.delete("/trainers/", status_code=204)
def remove_pokemon_of_trainer(pokemon_name: str, trainerName: str):
    pokemon_info = CONNECTOR.execute_select_one_query(SELECT_POKEMON_BY_NAME, [
        pokemon_name])
    trainer_info = CONNECTOR.execute_select_one_query(SELECT_TRAINER_BY_NAME, [
        trainerName])
    CONNECTOR.execute_insert_query(DELETE_POKEMON_OF_TRAINER, [
        trainer_info["trainer_id"], pokemon_info["pokemon_id"]])


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
