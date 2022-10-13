CREATE DATABASE IF NOT EXISTS sql_pokeTracker;

USE sql_pokeTracker;

-- -----------------------------------------------------
-- Table `sql_pokeTracker`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS Pokemons_info(
    pokemon_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    weight FLOAT(11) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Pokemons_types(
    pokemon_id INT NOT NULL ,
    type VARCHAR(50) NOT NULL,
    PRIMARY KEY(pokemon_id,type),
    FOREIGN KEY(pokemon_id) REFERENCES Pokemons_info(pokemon_id)
);

CREATE TABLE IF NOT EXISTS Trainers_info(
    trainer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    town VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Trainers_pokemons(
    trainer_id INT NOT NULL,
    pokemon_id INT NOT NULL,
    PRIMARY KEY(trainer_id,pokemon_id),
    FOREIGN KEY(pokemon_id) REFERENCES Pokemons_info(pokemon_id),
    FOREIGN KEY(pokemon_id) REFERENCES Trainers_info(trainer_id)
);

-- -----------------------------------------------------
-- VIEW
-- -----------------------------------------------------
CREATE VIEW Trainers_by_pokemon AS 
SELECT Pokemons_info.name as PokemonName, Trainers_info.name
FROM Trainers_pokemons, Trainers_info, Pokemons_info
JOIN Trainers_pokemons 
ON Pokemons_info.pokemons_id = Trainers_pokemons.pokemons_id
JOIN Trainers_info
ON Trainers_info.trainer_id = Trainers_pokemons.trainer_id
GROUP BY PokemonName;





