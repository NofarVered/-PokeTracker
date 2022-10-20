from fastapi import APIRouter, HTTPException, status
from API_DATA_RETRIEVE.my_sql_auth import my_sql_auth
from API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from API_DATA_RETRIEVE.utils.querys import *
from API_DATA_RETRIEVE.utils.pokemonAPI_tyeps import get_types

AUTH = my_sql_auth()
CONNECTOR = my_sql_proxy(AUTH)

router = APIRouter()


@router.get("/pokemons", status_code=200)
def get_pokemons_by_field(trainer_name: str = "", pokemon_type: str = ""):
    try:
        result = CONNECTOR.execute_select_all_query(SELECT_POKEMONS_BY_TRAINERS if trainer_name else SELECT_POKEMONS_BY_TYPE, [
            trainer_name if trainer_name else pokemon_type])
        return {"pokemons": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )


@router.get("/pokemons/{pokemon_name}", status_code=200)
def get_types_by_pokemon(pokemon_name):
    try:
        pokemon_record = CONNECTOR.execute_select_one_query(
            SELECT_POKEMON_BY_NAME, [pokemon_name])
        pokemon_id = pokemon_record["pokemon_id"]
        result = get_types(CONNECTOR, pokemon_id, pokemon_name)
        return {"types": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )


@router.get("/pokemons/heaviest", status_code=200)
def get_pokemons_by_type():
    try:
        result = CONNECTOR.execute_select_one_query(
            SELECT_HEAVIEST_POKEMON)
        return {"pokemon": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Exeception occured:{}".format(e)
        )


@router.get("/pokemons/popular", status_code=200)
def get_pokemons_by_type():
    try:
        result = CONNECTOR.execute_select_one_query(
            SELECT_POPULAR_POKEMON, [])
        return {"pokemon": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Exeception occured:{}".format(e)
        )
