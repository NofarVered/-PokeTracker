import json
from .utils.insert_querys import *
from ..API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from .utils.id_manager import Id_manager


class load_data:

    @staticmethod
    def load_pokemon_from_json_file(path: str, data_base: my_sql_proxy):
        f = open(path)
        pokemon_data = json.load(f)
        f.close()
        for pokemon in pokemon_data:
            pokemon_id = Id_manager.id_encoding(
                pokemon["name"], pokemon["weight"])
            load_data.load_pokemons_info_table(data_base, pokemon_id,
                                               pokemon["name"], pokemon["weight"])
            load_data.load_pokemon_type_table(
                data_base, pokemon_id, pokemon["type"])
            for trainer in pokemon["ownedBy"]:
                trainer_id = Id_manager.id_encoding(
                    trainer["name"], trainer["town"])
                load_data.load_trainers_info_table(data_base,
                                                   trainer_id, trainer["name"], trainer["town"])
                load_data.load_trainers_pokemons_table(
                    data_base, pokemon_id, trainer_id)

    @staticmethod
    def load_pokemons_info_table(CONNECTOR: my_sql_proxy, pokemon_id: str, pokemon_name: str, pokemon_weight: int):
        CONNECTOR.execute_query(INSERT_INTO_POKEMON_INFO, [
            pokemon_name, pokemon_weight])

    @staticmethod
    def load_trainers_info_table(CONNECTOR: my_sql_proxy, trainer_id: str, trainer_name: str, trainer_town: str):
        CONNECTOR.execute_query(INSERT_INTO_TRAINERS_INFO, [
            trainer_name, trainer_town])

    @staticmethod
    def load_pokemon_type_table(CONNECTOR: my_sql_proxy, pokemon_id: str, pokemon_type: str):
        CONNECTOR.execute_query(INSERT_INTO_POKEMON_TYPE, [
            pokemon_id, pokemon_type])

    @staticmethod
    def load_trainers_pokemons_table(CONNECTOR, pokemon_id: str, trainer_id: str):
        CONNECTOR.execute_query(INSERT_INTO_TRAINERS_POKEMONS, [
            pokemon_id, trainer_id])
