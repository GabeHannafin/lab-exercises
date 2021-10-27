
SELECT *
FROM persons;

SELECT *
FROM likes;

SELECT first_name
FROM persons
WHERE first_name LIKE "A%";

SELECT first_name
FROM persons
WHERE first_name LIKE "%A";


SELECT first_name
FROM persons
WHERE first_name LIKE "%A%";


SELECT first_name
FROM persons
WHERE first_name LIKE "_____";


SELECT first_name, street
FROM persons
WHERE street LIKE "%street%";

SELECT food
FROM likes
WHERE food LIKE "% %";

SELECT food
FROM likes
WHERE food LIKE "%te%";

SELECT *
FROM persons AS p CROSS JOIN likes as l
WHERE p.person_id == l.person_id;

SELECT food
FROM
    persons AS p
    JOIN likes AS l
    ON p.person_id == l.person_id
WHERE p.person_id == 345678;

SELECT first_name, food
FROM
    persons AS p
    JOIN likes AS l
    ON p.person_id == l.person_id
WHERE county == "Cork";

SELECT DISTINCT food
FROM
    persons AS p
    JOIN likes AS l
    ON p.person_id == l.person_id
WHERE gender == "F";

SELECT first_name
FROM
    persons AS p
    JOIN likes AS l
    ON p.person_id == l.person_id
WHERE food == "Pizza";

SELECT DISTINCT town
FROM
    persons AS p
    JOIN likes AS l
    ON p.person_id == l.person_id
WHERE food == "Beer";

SELECT *
FROM 
    likes AS L1
    JOIN likes AS L2
    ON L1.person_id == L2.person_id;

SELECT L1.person_id, L2.person_id
FROM
    likes AS L1
    JOIN likes AS L2
    ON L1.person_id == L2.person_id
WHERE L1.food == "Pizza" AND L2.food == "Nutella";