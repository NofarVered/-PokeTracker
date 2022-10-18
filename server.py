from fastapi import FastAPI, HTTPException, status
import requests
import uvicorn
from SRC.CREATE_DB_SCRIPT.load_data import load_data
from SRC.API_DATA_RETRIEVE.my_sql_auth import my_sql_auth
from SRC.API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from SRC.API_DATA_RETRIEVE.utils.querys import *

app = FastAPI()
db_auto = my_sql_auth()
CONNECTOR = my_sql_proxy(db_auto)
load_data(CONNECTOR)


@app.get("/")
def root():
    return "server is running"


@app.get("/pokemons/{trainer_name}")
def get_pokemons_by_trainer(trainer_name):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TRAINERS, [
            trainer_name])
        return {"pokemons": result}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid trainer name"
        )


@app.get("/pokemons/{pokemon_type}")
def get_pokemons_by_type(pokemon_type):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TYPE, [
            pokemon_type])
        return {"pokemons": result}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid pokemon type"
        )


@app.get("/trainers/{pokemon_name}")
def get_trainers_by_pokemon(pokemon_name):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TRAINERS, [
            pokemon_name])
    except requests.exceptions.HTTPError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid pokemon name"
        )


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
