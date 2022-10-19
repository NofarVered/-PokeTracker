# PokeTracker

## Technologies

<img align="left" alt="Pyton" width="50px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />
<img align="left" alt="Mysql" width="50px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/typescript/mysql.png" />


<br />
<br />

## Endpoints

Request:

```
GET http://localhost:8000/pokemons?trainer_name=Diantha
```

Response:

```
{
    "pokemons": [
        {
            "pokemon_name": "bulbasaur"
        },
        {
            "pokemon_name": "pinsir"
        },
        {
            "pokemon_name": "venusaur"
        },
        ...
    ]
}
```

Request:

```
GET http://localhost:8000/pokemons?pokemon_type=grass
```

Response:

```
{
    "pokemons": [
        {
            "name": "bulbasaur"
        },
        {
            "name": "exeggcute"
        },
        {
            "name": "exeggutor"
        },
        ...
    ]
}
```

Request:

```
GET http://localhost:8000/pokemons/heaviest
```

Response:

```
{
    "pokemon": {
        "LargestWeight": 4600.0,
        "name": "bulbasaur"
    }
}
```

Request:

```
GET http://localhost:8000/pokemons/popular
```

Response:

```
{
    "pokemon": {
        "pokemon_name": "abra",
        "number_of_trainers": 121
    }
}
```

Request:

```
GET http://localhost:8000/trainers?pokemon_name=bulbasaur
```

Response:

```
{
    "trainers": [
        {
            "trainer_name": "Bane"
        },
        {
            "trainer_name": "Archie"
        },
        {
            "trainer_name": "Ash"
        },
        {
            "trainer_name": "Giovanni"
        },
        {
            "trainer_name": "Diantha"
        },
        ...
    ]
}
```

Request:

```
POST http://localhost:8000/trainers?pokemon_name=bulbasaur

body:
    {
    "name" : "itay",
    "town" : "holon"
    }
```

Response:

```
{
    "name": "itay",
    "town": "holon",
    "trainer id": "aXRheWhvbG9u"
}
```

Request:

```
DELETE http://localhost:8000/trainers?pokemon_name=bulbasaur&trainer_name=Archie

```

Response:

```

No Content

```
