SELECT COUNT(movies.title), COUNT(actors.name)
from movies
JOIN actors
ON movies.id == actors.id;



SELECT COUNT(id)
FROM movies
WHERE yr == 1975;

SELECT c.movieid
FROM actors AS a
JOIN castings AS c
ON a.id == c.actorid
WHERE a.name == "Clint Eastwood";

SELECT m.title, m.yr
FROM actors AS a
JOIN castings AS c
JOIN movies AS m
ON a.id == c.actorid
AND m.id == c.movieid
WHERE a.name == "Clint Eastwood"
ORDER BY yr;

SELECT a.name
FROM actors AS a
JOIN castings AS c
JOIN movies AS m
ON a.id == c.actorid
AND m.id == c.movieid
WHERE m.title == "Citizen Kane";

SELECT a.name
FROM actors AS a
JOIN castings AS c
JOIN movies AS m
ON a.id == c.actorid
AND m.id == c.movieid
WHERE m.title == "Vertigo"
UNION
SELECT a.name
FROM actors AS a
JOIN castings AS c
JOIN movies AS m
ON a.id == c.actorid
AND m.id == c.movieid
WHERE m.title == "Rear Window";

SELECT title
FROM movies
WHERE director == 28;

