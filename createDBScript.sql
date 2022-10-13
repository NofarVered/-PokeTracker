CREATE DATABASE IF NOT EXISTS sql_pokeTracker;

USE sql_pokeTracker;


CREATE TABLE IF NOT EXISTS `sql_pokeTracker`.`Pokemons_info`
(
    'pokemon_id' INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    'name' VARCHAR(50) NOT NULL,
    'weight' FLOAT(11) DEFAULT 0,
)

