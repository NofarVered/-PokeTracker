import json
import typing
from insert_querys import *
from ..API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy


class load_data:

    @staticmethod
    def load_pokemon_from_json_file(path):
        f = open(path)
        pokemon_data = json.load(f)
        f.close()
        for pokemon in pokemon_data:
            load_data.load_pokemons_info_table(
                pokemon["name"], pokemon["weight"])

    @staticmethod
    def load_pokemons_info_table(CONNECTOR: my_sql_proxy, pokemon_name: str, pokemon_weight: int):
        CONNECTOR.execute_query(INSERT_INTO_POKEMON_INFO, [
            pokemon_name, pokemon_weight])

    @staticmethod
    def load_trainers_info_table(CONNECTOR: my_sql_proxy, trainer_name: str, trainer_town: str):
        CONNECTOR.execute_query(INSERT_INTO_TRAINERS_INFO, [
            trainer_name, trainer_town])

    # Itay
    # @staticmethod
    # def load_pokemon_type_table(pokemon_id, pokemon_type):
    #     pass

    # @staticmethod
    # def load_trainers_pokemons_table(CONNECTOR, name: str, town: str):
    #     pass
    # INSERT_INTO_TRAINERS_POKEMONS
    # should ask ! - nofar
