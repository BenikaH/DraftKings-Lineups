DROP TABLE IF EXISTS entries;
CREATE TABLE entries(
    game_id INT,
    username VARCHAR(30),
    points DECIMAL(5,2),
    pitcher_1 VARCHAR(30),
    pitcher_2 VARCHAR(30),
    catcher VARCHAR(30),
    first_base VARCHAR(30),
    second_base VARCHAR(30),
    third_base VARCHAR(30),
    shortstop VARCHAR(30),
    outfield_1 VARCHAR(30),
    outfield_2 VARCHAR(30),
    outfield_3 VARCHAR(30)
    );

DROP TABLE IF EXISTS games;
CREATE TABLE games(
    id INT PRIMARY KEY,
    game_date DATE,
    buyin VARCHAR(5),
    game_type VARCHAR(10),
    entries INT
);