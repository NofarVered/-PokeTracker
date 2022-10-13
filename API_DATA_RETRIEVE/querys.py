
# SELECT_HEAVIEST_POKEMON= nofar
SELECT_POKEMONS_BY_TYPE = """SELECT pokemons_info.name 
                            FROM pokemons_info 
                            JOIN pokemon_types 
                            ON pokemons_info.pokemons_id = pokemon_types.pokemons_id
                            WHERE type LIKE ($s)"""
# SELECT_TRAINERS_BY_POKEMON= nofar
SELECT_POKEMONS_BY_TRAINERS = """SELECT pokemons_info.name 
                            FROM pokemons_info 
                            JOIN trainer_pokemons 
                            ON pokemons_info.pokemons_id = trainer_pokemons.pokemons_id
                            JOIN trainers_info
                            ON trainers_info.trainer_id = trainer_pokemons.trainer_id
                            WHERE trainers_info.name LIKE ($s)"""
# SELECT_POPULAR_POKEMON= nofar + itay
