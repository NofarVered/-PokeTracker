from typing import List
import requests

from SRC.API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from SRC.CREATE_DB_SCRIPT.load_data import load_pokemon_type_table


def get_types_of_pokemon_from_pokemonAPI(pokemon_name: str):
    return requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json().get("types")


def extracts_types_from_list(types_list: List):
    extracts_types_list: List[str] = []
    for type in types_list:
        extracts_types_list.append(type["type"]["name"])
    return extracts_types_list


def insert_new_types_to_table(CONNECTOR: my_sql_proxy, pokemon_id: str, types_list: List):
    for pokemo_type in types_list:
        load_pokemon_type_table(CONNECTOR, pokemon_id, pokemo_type)


def get_pokemon(CONNECTOR: my_sql_proxy, pokemon_id: str, pokemon_name: str):
    types_list = get_types_of_pokemon_from_pokemonAPI(pokemon_name)
    extracts_types_list = extracts_types_from_list(types_list)
    insert_new_types_to_table(CONNECTOR, pokemon_id, extracts_types_list)
