CREATE TABLE astronauts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT
);


INSERT INTO astronauts VALUES ("José", "Jiménez");
INSERT INTO astronauts (firstname, lastname) VALUES ("Max", "Peck");


SELECT * FROM astronauts;

-- 1|José|Jiménez
-- 2|Max|Peck
