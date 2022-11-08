import pymysql
from fastapi import FastAPI, Request
import uvicorn
from starlette.responses import JSONResponse

from CREATE_DB_SCRIPT.load_data import load_data
from API_DATA_RETRIEVE.my_sql_proxy import CONNECTOR
from ROUTERS import trainers_router, pokemons_router, evolve_router

app = FastAPI()
# load_data(CONNECTOR)

app.include_router(trainers_router.router)
app.include_router(pokemons_router.router)
app.include_router(evolve_router.router)


@app.get("/")
def root():
    return "server is up and running"


@app.exception_handler(pymysql.MySQLError)
async def mysql_connector_error_handling(request: Request, exc: pymysql.MySQLError):
    return JSONResponse(
        status_code=500,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
