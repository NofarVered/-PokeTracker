
SELECT_HEAVIEST_POKEMON = """SELECT MAX(weight) AS LargestWeight, name 
                            FROM pokemons_info"""

SELECT_POKEMONS_BY_TYPE = """SELECT pokemons_info.name 
                            FROM pokemons_info 
                            JOIN pokemon_types 
                            ON pokemons_info.pokemons_id = pokemon_types.pokemons_id
                            WHERE type LIKE %s"""

SELECT_TRAINERS_BY_POKEMON = """SELECT pokemon_name, trainer_name 
                                FROM Trainers_by_pokemon_view 
                                WHERE pokemon_name LIKE %s """

SELECT_POKEMONS_BY_TRAINERS = """SELECT pokemons_info.name 
                            FROM Trainers_pokemons_view
                            WHERE trainer_name LIKE %s """

SELECT_POPULAR_POKEMON = """SELECT pokemon_name, COUNT(trainer_name) AS number_of_trainers
                            FROM Trainers_by_pokemon_view
                            ORDER BY number_of_trainers DESC
                            LIMIT 1 """

