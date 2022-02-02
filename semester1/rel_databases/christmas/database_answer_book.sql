--
--                CS1106/CS6503 Examination
--                Friday, 17 December 2021
--

-- Student Number: 121328481
-- Place X in box if registestered with DSS: [ ]

--                  Student Declaration
-- ==================================================================

-- This is to certify that the work I am submitting is my own and has 
-- been done by me solely and not in consultation with anyone else. 
-- Neither I nor anyone else have submitted this work for assessment, 
-- either at University College Cork or elsewhere. I have read and 
-- understood the regulations of University College Cork concerning 
-- plagiarism.  Where breaches of the declaration are detected, these 
-- will be reviewed under UCC student conduct and plagiarism policies. 
-- Any breach of the examination rules is a serious issue and can incur 
-- penalties.

-- ALL ANSWERS SUBMITTED WILL BE CHECKED FOR COMPLIANCE WITH UNIVERSITY
-- PLAGIARISM POLICY.

-- ==================================================================
-- QUESTION ONE
-- ------------------------------------------------------------------
-- Part (i) 
-- see question1.jpg

-- Part (ii)
-- see question1.jpg

-- ==================================================================
-- -- QUESTION TWO
-- -- ------------------------------------------------------------------
-- -- Part (i) 
-- INSERT INTO children()
-- VALUES(100, "mike", "schubert", 2020-06-12, "Male", 2.0)
--       (101, "scont", "hubink", 2012-02-13, "Female", 0.1)
--       (102, "Frank", "Wutherbuss", 2001-01-12, "Male", 0.8)
-- 
-- 
-- -- Part (ii)
-- DElETE FROM children
-- WHERE niceness < 0.25;
-- 
-- 
-- -- Part (iii) 
-- UPDATE children
-- SET niceness = niceness - (niceness * 0.10)
-- WHERE gender == "Male";
-- 
-- 
-- -- Part (iv)
-- SELECT name, niceness
-- FROM children
-- WHERE dob > 2011-12-25;
-- 
-- 
-- -- Part (v) 
-- SELECT COUNT(*), gender
-- WHERE gender == "Female"
-- UNION
-- SELECT COUNT(*), gender
-- WHERE gender == "Male";
-- 
-- 
-- ==================================================================
-- QUESTION THREE
-- ------------------------------------------------------------------

-- Part (i) 
SELECT c.name
FROM countries as c JOIN
country_languages AS l
ON c.code == l.country_code
WHERE l.percentage > 25 AND l.language == "French"; 

-- Part (ii)
SELECT coun.continent, COUNT(*)
FROM countries as coun JOIN
cities AS cit
ON cit.country_code == coun.code
WHERE cit.population > 5000000
GROUP BY continent;



-- Part (iii) 
SELECT DISTINCT L.language, c.population,c.name, L.percentage
FROM country_languages AS L JOIN
countries AS c
ON L.country_code == c.code
ORDER BY (L.percentage/100)*(c.population);


-- Part (iv)
SELECT ci.name, MAX(ci.population)
FROM countries AS c JOIN
cities AS ci
ON ci.id == c.capital;



-- Part (v)
SELECT cl.language, cl.percentage, c.continent
FROM country_languages AS cl JOIN
countries as c
ON cl.country_code = c.code
WHERE cl.percentage > 15
GROUP BY cl.language
HAVING COUNT(*) >= 3;





-- Part (vi)
SELECT continent, name, MAX(life_expectancy)
FROM countries
GROUP BY continent;


