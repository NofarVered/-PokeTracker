from multiprocessing import current_process
from tkinter.messagebox import RETRY
from unittest import result
import requests

# from SRC.API_DATA_RETRIEVE.my_sql_proxy import my_sql_proxy
# from SRC.CREATE_DB_SCRIPT.load_data import load_pokemon_type_table


def get_evolution_chain(pokemon_name: str):
    url_evolution = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()["species"]["url"]
    return requests.get(url_evolution).json()[
        "evolution_chain"]["url"]


def get_evolution(pokemon_name: str):
    evolution_chain = requests.get(
        get_evolution_chain(pokemon_name)).json()["chain"]
    current_pokemon = evolution_chain["species"]["name"]
    while (current_pokemon != pokemon_name and len(evolution_chain["evolves_to"]) != 0):
        evolution_chain = evolution_chain["evolves_to"][0]
        current_pokemon = evolution_chain["species"]["name"]
    return pokemon_name if len(evolution_chain["evolves_to"]) == 0 else evolution_chain["evolves_to"][0]["species"]["name"]
