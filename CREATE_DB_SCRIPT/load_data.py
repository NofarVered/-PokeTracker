import json


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

    # @staticmethod
    # def load_pokemons_info_table(pokemon_name, pokemon_weight):

    #     # @staticmethod
    #     # def load_trainers_info_table(): nofar

    # @staticmethod
    # def load_pokemon_type_table(pokemon_id, pokemon_type):

    #     # @staticmethod
    #     # def load_pokemon_pokemons_table(): nofar
