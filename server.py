from sqlite3 import dbapi2
from fastapi import FastAPI
import uvicorn
from SRC.CREATE_DB_SCRIPT.load_data import load_pokemon_from_json_file
from SRC.API_DATA_RETRIEVE.my_sql_auth import my_sql_auth
from SRC.API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy


app = FastAPI()


@app.get('/')
def root():
    return "Hello Pokemon"

# @app.get('/pokemons/{pokemon_name}')
# def get_pokemon_info():


if __name__ == "__main__":
    # uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)
    db_auto = my_sql_auth()
    CONNECTOR = my_sql_proxy(db_auto)
    load_pokemon_from_json_file(
        "SRC\CREATE_DB_SCRIPT\services\poke_data.json", CONNECTOR)
