import json
import typing
from insert_querys import *
import pymysql as mysql
import mysql.connector


class load_data:

    @staticmethod
    def load_pokemon_from_json_file(path):
        f = open(path)
        pokemon_data = json.load(f)
        f.close()
        for pokemon in pokemon_data:
            load_data.load_pokemons_info_table(
                pokemon["name"], pokemon["weight"])
            load_data.load_pokemon_type_table("???", pokemon["type"])

    # Itay
    # @staticmethod
    # def load_pokemons_info_table(pokemon_name, pokemon_weight):
    #   pass

    @staticmethod
    def load_trainers_info_table(CONNECTOR, name: str, town: str):
        mycursor = CONNECTOR.cursor()
        mycursor.execute(INSERT_INTO_TRAINERS_INFO, [name, town])
        mycursor.close()

    # Itay
    # @staticmethod
    # def load_pokemon_type_table(pokemon_id, pokemon_type):
    #     pass

    # @staticmethod
    # def load_trainers_pokemons_table(CONNECTOR, name: str, town: str):
    #     pass
    # INSERT_INTO_TRAINERS_POKEMONS
    # should ask ! - nofar
