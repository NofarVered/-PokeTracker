import json
from .queries.insert_querys import *
from API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from .services.id_manager import Id_manager


def load_pokemon_from_json_file(path: str, data_base: my_sql_proxy):
    f = open(path)
    pokemon_data = json.load(f)
    f.close()
    for pokemon in pokemon_data:
        load_pokemons_info_table(data_base, pokemon["id"],
                                 pokemon["name"], pokemon["weight"])
        load_pokemon_type_table(
            data_base, pokemon["id"], pokemon["type"])
        for trainer in pokemon["ownedBy"]:
            trainer_id = Id_manager.id_encoding(
                trainer["name"], trainer["town"])
            load_trainers_info_table(data_base,
                                     trainer_id, trainer["name"], trainer["town"])
            load_trainers_pokemons_table(
                data_base, trainer_id, pokemon["id"])


def load_pokemons_info_table(CONNECTOR: my_sql_proxy, pokemon_id: str, pokemon_name: str, pokemon_weight: int):
    CONNECTOR.execute_insert_query(INSERT_INTO_POKEMON_INFO, [
        pokemon_id, pokemon_name, pokemon_weight])


def load_trainers_info_table(CONNECTOR: my_sql_proxy, trainer_id: str, trainer_name: str, trainer_town: str):
    CONNECTOR.execute_insert_query(INSERT_INTO_TRAINERS_INFO, [
        trainer_id, trainer_name, trainer_town])


def load_pokemon_type_table(CONNECTOR: my_sql_proxy, pokemon_id: str, pokemon_type: str):
    CONNECTOR.execute_insert_query(INSERT_INTO_POKEMON_TYPE, [
        pokemon_id, pokemon_type])


def load_trainers_pokemons_table(CONNECTOR: my_sql_proxy, pokemon_id: str, trainer_id: str):
    CONNECTOR.execute_insert_query(INSERT_INTO_TRAINERS_POKEMONS, [
        pokemon_id, trainer_id])


def load_data(CONNECTOR: my_sql_proxy):
    load_pokemon_from_json_file(
        "CREATE_DB_SCRIPT\services\poke_data.json", CONNECTOR)
