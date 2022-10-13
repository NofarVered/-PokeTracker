
SELECT_HEAVIEST_POKEMON = """SELECT MAX(weight) AS LargestWeight, name 
                            FROM pokemons_info"""

SELECT_POKEMONS_BY_TYPE = """SELECT pokemons_info.name 
                            FROM pokemons_info 
                            JOIN pokemon_types 
                            ON pokemons_info.pokemons_id = pokemon_types.pokemons_id
                            WHERE type LIKE ($s)"""

SELECT_TRAINERS_BY_POKEMON = """SELECT pokemon_name, trainer_name 
                                FROM Trainers_by_pokemon 
                                WHERE pokemon_name = %s """

SELECT_POKEMONS_BY_TRAINERS = """SELECT pokemons_info.name 
                            FROM pokemons_info 
                            JOIN trainer_pokemons 
                            ON pokemons_info.pokemons_id = trainer_pokemons.pokemons_id
                            JOIN trainers_info
                            ON trainers_info.trainer_id = trainer_pokemons.trainer_id
                            WHERE trainers_info.name LIKE ($s)"""

SELECT_POPULAR_POKEMON = """SELECT pokemon_name, COUNT(trainer_name) AS number_of_trainers
                            FROM Trainers_by_pokemon 
                            ORDER BY number_of_trainers DESC
                            LIMIT 1 """
