-- EXERCISE XP

-- Exercise 1: DVD Rental

-- ITEM 1

SELECT DISTINCT name
FROM language


-- ITEM 2

SELECT f.title , f.description , l.name
FROM film f
JOIN language l
ON f.language_id = l.language_id


-- ITEM 3

SELECT f.title , f.description , l.name
FROM language l
LEFT JOIN film f
ON f.language_id = l.language_id


-- ITEM 4

CREATE TABLE new_film (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
)

INSERT INTO new_film (name) VALUES
	('World Cup 1958'),
	('World Cup 1962'),
	('World Cup 1970'),
	('World Cup 1994'),
	('World Cup 2002')


-- ITEM 5

CREATE TABLE customer_review (
	review_id SERIAL PRIMARY KEY,
	film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title TEXT NOT NULL,
	score INTEGER NOT NULL CHECK (score BETWEEN 1 and 10),
	review_text TEXT,
	last_update DATE NOT NULL,
	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE SET NULL ON UPDATE CASCADE
)


-- ITEM 6

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update) VALUES
	(1,1,'Fifa review',8,'The quality of the video is too low','2000-10-10'),
	(5,3,'German fell to Brazil in the Final',10,'The definition and emotions passed by the film are incredibly real','2010-07-07')


-- ITEM 7 -- The review was deleted as well due to the 'ON DELETE CASCADE'

DELETE FROM new_film
WHERE id = 1

SELECT film_id, description , language_id
FROM film

-- Exercise 2: DVD Rental

-- ITEM 1

UPDATE film
SET language_id = 5
WHERE description ILIKE '%japan%'

UPDATE film
SET language_id = 4
WHERE description ILIKE '%china%'


-- ITEM 2
-- There are 2 FOREIGN KEYS: address_id and store_id
-- When adding new records to the table customers, we can only add values with a valid store_id
-- and we cannot add a second value with an existing address_id.


-- ITEM 3

DROP TABLE if exists customer_review 
-- It is an easy step because no other table pulls information from this table.


-- ITEM 4

SELECT COUNT(rental_id) AS outstanding_rental
FROM rental
WHERE return_date IS NULL


-- ITEM 5

SELECT r.rental_id, r.inventory_id, f.film_id , f.rental_rate
FROM rental r
JOIN inventory i
ON r.inventory_id = i.inventory_id
JOIN film f
ON i.film_id = f.film_id
WHERE return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30


-- ITEM 6

-- ITEM 6.1

SELECT f.film_id , f.title , f.description , fa.actor_id , a.first_name , a.last_name
FROM film f
JOIN film_actor fa
ON f.film_id = fa.film_id
JOIN actor a
ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe' AND f.description ILIKE '%sumo wrestler%'


-- ITEM 6.2

SELECT f.film_id , f.title , f.description , f.length , f.rating , fc.category_id , c.name
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN category c
ON fc.category_id = c.category_id
WHERE length < 60 AND rating = 'R' AND c.name ILIKE 'documentary'


-- ITEM 6.3

SELECT f.film_id , f.title , c.first_name , c.last_name , r.return_date , p.amount
FROM film f
JOIN inventory i
ON f.film_id = i.film_id
JOIN rental r
ON i.inventory_id = r.inventory_id
JOIN payment p
ON r.rental_id = p.rental_id
JOIN customer c
ON r.customer_id = c.customer_id
WHERE r.return_date >= '2005-07-28' AND r.return_date <= '2005-08-01' AND p.amount > 4 AND c.first_name = 'Matthew' AND c.last_name = 'Mahan'


-- ITEM 6.4

SELECT f.film_id , f.title , f.description , f.replacement_cost , c.first_name , c.last_name
FROM film f
JOIN inventory i
ON f.film_id = i.film_id
JOIN rental r
ON i.inventory_id = r.inventory_id
JOIN customer c
ON r.customer_id = c.customer_id
WHERE (f.description ILIKE '%boat%' OR f.title ILIKE '%boat%') AND c.first_name = 'Matthew' AND c.last_name = 'Mahan'
ORDER BY f.replacement_cost DESC
