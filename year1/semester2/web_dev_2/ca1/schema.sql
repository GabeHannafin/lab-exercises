DROP TABLE IF EXISTS hitmen;

CREATE TABLE hitmen
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO hitmen(name, description)
VALUES
    ("Brutus", "Do not be decieved by his rugged handsomeness, Brutus is a fiend. He prides himself on being the most cruel man on the team. He will do anything for a price. If you want to give your target one last kind gesture or final insult spend the extra euros on elite hitman Brutus. "),
    ("Cerberus", "Not the best, not the worst. Cerberus takes a detached stance towards his work.  He's honestly just doing this as a side gig to fund his bubble tea habit. As such, his thirst for tapioca makes him one of the most ruthless killers alive.  Best known for his talent in the disposal of children."),
    ("Aphrodite", "His dashing looks and deceitful demeanor make him one of the most covert and effective hitmen in the country.  This femboy fatale specializes in homicides involving wacky hijinks. Like the goddess herself, Aphrodite is the pinnacle of beauty and inflicting suffering.")
;

DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    username TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users(username, password)
VALUES
    ("admin", "pbkdf2:sha256:260000$LPCr4TNrKL5FFhbk$51c128c6d9d20492a272063ead8ad0f89dbb35131237912411c83f410973c64a"),
    ("ghost", "pbkdf2:sha256:260000$5XvJpb2lDPJblcqm$01e3c255f00d1a6c47e840ad18268acb6ed103940a24bef8bb99f2f338cb26f2")
;

