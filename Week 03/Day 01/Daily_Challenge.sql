-- DAILY CHALLENGE: Actors

-- ITEM 1

SELECT COUNT(first_name)
FROM actors


-- ITEM 2 - We will see an error because the fields were set as NOT NULL
-- Entering a record with a NULL VALUE violates a not-null constraint

INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
VALUES ('Leonardo', 'DiCaprio',NULL,3)


