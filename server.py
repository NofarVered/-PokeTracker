from fastapi import FastAPI
import uvicorn
from SRC.CREATE_DB_SCRIPT.load_data import load_data
from SRC.API_DATA_RETRIEVE.my_sql_auth import my_sql_auth
from SRC.API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy


app = FastAPI()
db_auto = my_sql_auth()
CONNECTOR = my_sql_proxy(db_auto)
load_data(CONNECTOR)


@app.get('/')
def root():
    return "Hello Pokemon"


@app.get('/pokemons/')
def get_pokemon_info(name: str):
    return "Hii"+name


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)
