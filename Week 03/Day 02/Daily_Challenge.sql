CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


SELECT * FROM SecondTab


----- QUESTION 1: What will be the OUTPUT of the following statement?
-----    SELECT COUNT(*) 
-----    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- My answer:
-- The output will be a table 1x1: 1 line (plus header)  vs  1 column
-- The result will look like: 
--
-- COUNT
--   3
--
-- Logic: The subquery used on the WHERE CLAUSE will be a list with only the NULL element: (NULL)
-- Therefore, the main query will count total of elements valid values (different than NULL) in which id is different than NULL

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- Result: 0 
-- My answer was wrong --

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 


----- QUESTION 2: What will be the OUTPUT of the following statement?
-----    SELECT COUNT(*) 
-----    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- My answer:
-- The output will be a table 1x1: 1 line (plus header)  vs  1 column
-- The result will look like: 
--
-- COUNT
--   2
--
-- Logic: The subquery used on the WHERE CLAUSE will be a list with only one element: (5)
-- Therefore, the main query will count total of elements valid values (different than NULL) where id is different than 5 (not countering NULL as well)
-- The query will count 2 elements, id = 6 and id = 7

	SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Result: 2
-- My answer was correct --

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 


----- QUESTION 3: What will be the OUTPUT of the following statement?
-----    SELECT COUNT(*) 
-----    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- My answer:
-- The output will be a table 1x1: 1 line (plus header)  vs  1 column
-- The result will look like: 
--
-- COUNT
--   2
--
-- Logic: The subquery used on the WHERE CLAUSE will be a list with 2 elements: (5,NULL)
-- Therefore, the main query will count total of elements valid values (different than NULL) where id is different than 5 and NULL (again)
-- The query will count 2 elements, id = 6 and id = 7

  	SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
	
-- Result: 0
-- My answer was wrong --

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 


----- QUESTION 4: What will be the OUTPUT of the following statement?
-----    SELECT COUNT(*) 
-----    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- My answer:
-- The output will be a table 1x1: 1 line (plus header)  vs  1 column
-- The result will look like: 
--
-- COUNT
--   2
--
-- Logic: The subquery used on the WHERE CLAUSE will be a list with  only one element: (5)
-- Therefore, the main query will count total of elements valid values (different than NULL) where id is different than 5 and NULL (again)
-- The query will count 2 elements, id = 6 and id = 7

	SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- Result: 2
-- My answer was correct --

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- I can see both cases my guesses were wrong where when the subquery contained the element NULL
