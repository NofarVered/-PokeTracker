
SELECT_HEAVIEST_POKEMON = """SELECT MAX(weight) AS LargestWeight, name 
                            FROM pokemons_info"""

SELECT_POKEMONS_BY_TYPE = """SELECT pokemons_info.name 
                            FROM pokemons_info 
                            JOIN pokemons_types 
                            ON pokemons_info.pokemon_id = pokemons_types.pokemon_id
                            WHERE type LIKE %s"""

SELECT_TRAINERS_BY_POKEMON = """SELECT trainer_name 
                                FROM Trainers_pokemons_view 
                                WHERE pokemon_name LIKE %s """

SELECT_POKEMONS_BY_TRAINERS = """SELECT pokemon_name 
                            FROM Trainers_pokemons_view
                            WHERE trainer_name LIKE %s """

SELECT_POPULAR_POKEMON = """SELECT pokemon_name, COUNT(trainer_name) AS number_of_trainers
                            FROM Trainers_by_pokemon_view
                            ORDER BY number_of_trainers DESC
                            LIMIT 1 """

SELECT_POKEMON_BY_NAME = """SELECT * 
                                FROM Pokemons_info 
                                WHERE name LIKE %s """

SELECT_TRAINER_BY_NAME = """SELECT * 
                                FROM Trainers_info 
                                WHERE name LIKE %s """

DELETE_POKEMON_OF_TRAINER = """DELETE FROM trainers_pokemons WHERE trainer_id LIKE %s AND pokemon_id LIKE %s ;"""
