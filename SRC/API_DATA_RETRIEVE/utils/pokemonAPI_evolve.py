import requests


def get_evolution_chain(pokemon_name: str):
    try:
        url_evolution = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()["species"]["url"]
        return requests.get(url_evolution).json()[
            "evolution_chain"]["url"]
    except Exception as e:
        return e


def get_evolution(pokemon_name: str):
    try:
        evolution_chain = requests.get(
            get_evolution_chain(pokemon_name)).json()["chain"]
        current_pokemon = evolution_chain["species"]["name"]

        while (current_pokemon != pokemon_name and len(evolution_chain["evolves_to"]) != 0):
            evolution_chain = evolution_chain["evolves_to"][0]
            current_pokemon = evolution_chain["species"]["name"]

        return pokemon_name if len(evolution_chain["evolves_to"]) == 0 else evolution_chain["evolves_to"][0]["species"]["name"]

    except Exception as e:
        return e
