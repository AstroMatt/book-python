-- SQLite3
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(20),
    lastname VARCHAR(50),
    pesel INTEGER UNIQUE,
    age INTEGER
);

-- SQLite3
CREATE TABLE IF NOT EXISTS sensor_data (
    datetime DATETIME PRIMARY KEY,
    sync_datetime DATETIME DEFAULT NULL,
    device VARCHAR(255),
    parameter VARCHAR(255),
    value REAL,
    unit VARCHAR(255)
);

-- MySQL
CREATE DATABASE astronauts;

-- MySQL
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
