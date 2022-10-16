from API_DATA_RETRIEVE import my_sql_auth
from SRC.API_DATA_RETRIEVE import my_sql_proxy
from SRC.CREATE_DB_SCRIPT import load_data


my_auto_to_db = my_sql_auth()
my_connector = my_sql_proxy(my_auto_to_db)

load_data.load_pokemon_from_json_file("../poke_data.json", my_connector)
