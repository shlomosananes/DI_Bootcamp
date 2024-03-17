-- ITEM 1

-- Database: public

CREATE DATABASE public
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Israel.1252'
    LC_CTYPE = 'English_Israel.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


-- ITEM 2

CREATE TABLE items (
	item_id SERIAL PRIMARY KEY,
	item_description VARCHAR(100) NOT NULL,
	item_price INTEGER NOT NULL
)

CREATE TABLE customers (
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (100) NOT NULL
)


-- ITEM 2.1

INSERT INTO items (item_description,item_price) VALUES 
	('Small Desk',100),
	('Large desk', 300),
	('Fan', 80)


-- ITEM 2.2

INSERT INTO customers (first_name, last_name) VALUES
	('Greg','Jones'),
	('Sandra','Jones'),
	('Scott','Scott'),
	('Trevor','Green'),
	('Melanie','Johnson')


-- ITEM 2.3

-- 2.3.1

SELECT * 
FROM items


-- 2.3.2

SELECT * 
FROM items
WHERE item_price > 80


-- 2.3.3

SELECT * 
FROM items
WHERE item_price <= 300


-- 2.3.4 (The outcome will be an empty customers table)

SELECT * 
FROM customers
WHERE last_name = 'Smith'


-- 2.3.5

SELECT * 
FROM customers
WHERE last_name = 'Jones'


-- 2.3.6

SELECT * 
FROM customers
WHERE first_name != 'Scott'
