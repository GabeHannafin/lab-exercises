DROP TABLE IF EXISTS hitmen;

CREATE TABLE hitmen
(
    name TEXT PRIMARY KEY NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO hitmen(name, description)
VALUES
    ("Intercourse Enthusiast", "Integer tempor est diam, eu lacinia lorem lacinia in. Aenean pharetra erat justo, id sodales nisl luctus a. Pellentesque ut tempus nisi, vel semper lacus. Curabitur id orci risus. In vel dapibus lorem. Donec non ullamcorper nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam et pulvinar massa. Cras ultricies iaculis lacus, in porttitor elit luctus eget. Mauris ullamcorper risus nisi, vitae egestas nulla sodales sed. Nam lectus libero, porttitor sed mauris vel, tempor sodales nisl. Quisque odio lacus, fringilla eget tincidunt eu, dignissim vel leo."),
    ("Mike", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tempus pulvinar erat, at viverra tellus aliquet et. Mauris id urna in nunc condimentum consequat sit amet non ex. In malesuada, velit id condimentum blandit, magna dui bibendum turpis, nec mollis metus felis vel sapien. Donec et congue erat. Duis in eros maximus nisl eleifend condimentum et eu nisl. Vestibulum interdum arcu et risus mattis egestas. Phasellus nisl est, malesuada at ornare et, euismod id nisl. Mauris at eros dictum, posuere mi at, dignissim lectus."),
    ("SYd", "Integer tempor est diam, eu lacinia lorem lacinia in. Aenean pharetra erat justo, id sodales nisl luctus a. Pellentesque ut tempus nisi, vel semper lacus. Curabitur id orci risus. In vel dapibus lorem. Donec non ullamcorper nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam et pulvinar massa. Cras ultricies iaculis lacus, in porttitor elit luctus eget. Mauris ullamcorper risus nisi, vitae egestas nulla sodales sed. Nam lectus libero, porttitor sed mauris vel, tempor sodales nisl. Quisque odio lacus, fringilla eget tincidunt eu, dignissim vel leo.")
;

DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    username TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOL NOT NULL
);

INSERT INTO users(username, password, is_admin)
VALUES
    ("admin", "pbkdf2:sha256:260000$LPCr4TNrKL5FFhbk$51c128c6d9d20492a272063ead8ad0f89dbb35131237912411c83f410973c64a", "True")
;

