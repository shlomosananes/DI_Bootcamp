-- EXERCISE 1: Bootcamp

-- SECTION CREATE

-- ITEM 1

-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

CREATE DATABASE bootcamp
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Israel.1252'
    LC_CTYPE = 'English_Israel.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


-- ITEMS 2 and 3

CREATE TABLE students (
	id SERIAL NOT NULL,
	last_name VARCHAR (100) NOT NULL,
	first_name VARCHAR (25) NOT NULL,
	birth_date DATE NOT NULL
)


-- SECTION INSERT

-- ITEM 1

INSERT INTO students (last_name, first_name, birth_date) VALUES
	('Benichou','Marc', '02/11/1998'),
	('Cohen','Yoan', '03/12/2010'),
	('Benichou','Lea', '27/07/1987'),
	('Dux','Amelia', '07/04/1996'),
	('Grez','David', '14/06/2003'),
	('Simpson','Omer', '03/10/1980')

-- ITEM 2

INSERT INTO students (last_name, first_name, birth_date) VALUES
	('Sananes','Shlomo', '07/11/1989')
	

-- SECTION SELECT

-- ITEM 1
	
SELECT * 
FROM students


-- ITEM 2
	
SELECT first_name , last_name
FROM students


-- ITEM 3

-- ITEM 3.1

SELECT first_name , last_name
FROM students
WHERE id = 2


-- ITEM 3.2

SELECT first_name , last_name
FROM students
WHERE last_name = 'Benichou' AND first_name = 'Marc'


-- ITEM 3.3

SELECT first_name , last_name
FROM students
WHERE last_name = 'Benichou' OR first_name = 'Marc'


-- ITEM 3.4

SELECT first_name , last_name
FROM students
WHERE first_name ILIKE '%a%'


-- ITEM 3.5

SELECT first_name , last_name
FROM students
WHERE first_name ILIKE 'a%'


-- ITEM 3.6

SELECT first_name , last_name
FROM students
WHERE first_name ILIKE '%a'


-- ITEM 3.7

SELECT first_name , last_name
FROM students
WHERE SUBSTRING(first_name, LENGTH(first_name) -1, 1) = 'a'


-- ITEM 3.8

SELECT first_name , last_name
FROM students
WHERE id = 1 OR id = 3


-- ITEM 4

SELECT * 
FROM students
WHERE birth_date >= '01/01/2000'


