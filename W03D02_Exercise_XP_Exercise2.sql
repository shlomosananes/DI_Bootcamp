-- Exercise XP (Exercise 2 using Database 'dvdrental')

-- ITEM 1

SELECT *
FROM customer

-- ITEM 2

SELECT first_name, last_name, CONCAT(first_name,' ',last_name) AS full_name
FROM customer

-- ITEM 3

SELECT DISTINCT create_date
FROM customer

-- ITEM 4

SELECT *
FROM customer
ORDER BY first_name DESC

-- ITEM 5

SELECT film_id , title, description , release_year , rental_rate
FROM film
ORDER BY rental_rate 

-- ITEM 6

SELECT address , phone
FROM address
WHERE district = 'Texas'

-- ITEM 7 

SELECT *
FROM film
WHERE film_id IN (15,150)

-- ITEM 8

SELECT film_id , title , description , length , rental_rate
FROM film
WHERE title = 'Inglourious Basterds'

-- ITEM 9 

SELECT film_id , title , description , length , rental_rate
FROM film
WHERE LEFT(title,2) = LEFT('Inglourious Basterds',2)

-- ITEM 10

SELECT * 
FROM film
ORDER BY rental_rate
LIMIT 20

-- ITEM 11

SELECT * 
FROM film
ORDER BY rental_rate
LIMIT 10 OFFSET 10

-- ITEM 12

SELECT c.customer_id , c.first_name , c.last_name , p.amount , p.payment_date
FROM customer c
JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id

-- ITEM 13

SELECT f.film_id , f.title , COUNT(i.film_id)
FROM film f
JOIN inventory i
ON f.film_id = i.film_id
GROUP BY f.film_id , f.title
HAVING COUNT(i.film_id) = 5

-- ITEM 14

SELECT co.country , ci.city
FROM city ci
JOIN country co
ON ci.country_id = co.country_id
ORDER BY co.country , ci.city

-- ITEM 15

SELECT r.staff_id , s.first_name AS staff_name , r.customer_id , c.first_name AS customer_first_name , c.last_name AS customer_last_name  , p.amount , p.payment_date
FROM rental r
JOIN customer c
ON r.customer_id = c.customer_id
JOIN staff s
ON r.staff_id = s.staff_id
JOIN payment p
ON r.rental_id = p.rental_id
ORDER BY staff_id , customer_id


