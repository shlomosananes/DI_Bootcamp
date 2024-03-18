-- Exercise XP (Exercise 1 using Database 'public')

-- Exercise 1: Items And Customers

-- ITEM 1

SELECT *
FROM items
ORDER BY item_price

-- ITEM 2

SELECT *
FROM items
WHERE item_price >= 80
ORDER BY item_price DESC

-- ITEM 3

SELECT first_name , last_name
FROM customers
ORDER BY first_name
LIMIT 3

-- ITEM 4

SELECT last_name
FROM customers
ORDER BY last_name DESC

