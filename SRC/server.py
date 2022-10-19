from fastapi import FastAPI
import uvicorn
from CREATE_DB_SCRIPT.load_data import load_data
from API_DATA_RETRIEVE.my_sql_auth import my_sql_auth
from API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
from ROUTERS import trainers_router, pokemons_router

app = FastAPI()
AUTH = my_sql_auth()
CONNECTOR = my_sql_proxy(AUTH)
# load_data(CONNECTOR)

app.include_router(trainers_router.router)
app.include_router(pokemons_router.router)


@app.get("/")
def root():
    return "server is up and running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
