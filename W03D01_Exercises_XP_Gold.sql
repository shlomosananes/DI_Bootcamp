-- EXERCISE XP Gold

-- Exercise 1: Bootcamp

-- SECTION SELECT

-- ITEM 1

SELECT first_name, last_name, birth_date
FROM students
ORDER BY last_name
LIMIT 4


-- ITEM 2 -- Using Subqueries

SELECT *
FROM students
WHERE birth_date = ( SELECT MAX(birth_date) FROM students )


-- ITEM 3 

SELECT *
FROM students
LIMIT 3 OFFSET 2