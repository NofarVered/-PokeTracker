from typing import List
import requests

from API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from CREATE_DB_SCRIPT.load_data import load_pokemon_type_table


def get_types_from_pokemonAPI(pokemon_name: str):
    return requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()["types"]


def pharse_types(types_list: List):
    extracts_types_list: List[str] = []
    for type in types_list:
        extracts_types_list.append(type["type"]["name"])
    return extracts_types_list


def insert_types_record(CONNECTOR: my_sql_proxy, pokemon_id: str, types_list: List):
    for pokemo_type in types_list:
        load_pokemon_type_table(CONNECTOR, pokemon_id, pokemo_type)


def get_types(CONNECTOR: my_sql_proxy, pokemon_id: str, pokemon_name: str):
    types_list = get_types_from_pokemonAPI(pokemon_name)
    extracts_types_list = pharse_types(types_list)
    insert_types_record(CONNECTOR, pokemon_id, extracts_types_list)
    return extracts_types_list
