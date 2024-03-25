-- Week 03 - Day 03 - Dailly Challenge: 

-- Daily Challenge: Tables Relationships

-- PART 1

-- Item 1

CREATE TABLE customer (
	id SERIAL PRIMARY KEY,
	first_name varchar(25) NOT NULL,
	last_name varchar(50) NOT NULL
)

CREATE TABLE customer_profile (
	id SERIAL,
	isLoggedIn BOOLEAN DEFAULT false,
	pk_customer_id INTEGER NOT NULL,
	PRIMARY KEY (pk_customer_id),
	CONSTRAINT fk_customer_id FOREIGN KEY (pk_customer_id) REFERENCES customer(id)
)


-- Item 2

INSERT INTO customer (first_name , last_name) VALUES 
	('Doe','John'),
	('Lalu','Jerome'),
	('Rive','Lea')


-- Item 3

INSERT INTO customer_profile (isLoggedIn, pk_customer_id) VALUES
	(TRUE, (SELECT id FROM customer WHERE last_name = 'John')),
	(FALSE, (SELECT id FROM customer WHERE last_name = 'Jerome'))


-- Item 4

SELECT c.first_name
FROM customer c
JOIN customer_profile cp
ON c.id = pk_customer_id
WHERE cp.isLoggedIn = TRUE


-- Item 5

SELECT c.first_name , cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp
ON c.id = pk_customer_id


-- Item 6

SELECT COUNT (*)
FROM customer c
LEFT JOIN customer_profile cp
ON c.id = pk_customer_id
WHERE cp.isLoggedIn != TRUE





-- PART 2

-- Item 1

CREATE TABLE book (
	book_id SERIAL PRIMARY KEY,
	title varchar(50) NOT NULL,
	author varchar(100) NOT NULL
)


-- Item 2

INSERT INTO book (title, author) VALUES
	('Alice In Wonderland' , 'Lewis Carroll'),
	('Harry Potter' , 'J.K Rowling'),
	('To kill a mockingbird' , 'Harper Lee')


-- Item 3

CREATE TABLE student (
	student_id SERIAL PRIMARY KEY,
	name varchar(50) NOT NULL UNIQUE,
	age integer check (age <=15)
)


-- Item 4

INSERT INTO student (name, age) VALUES
	('John',12),
	('Lera',11),
	('Patrick',10),
	('Bob',14)


-- Item 5

CREATE TABLE library (
	book_fk_id INT NOT NULL, 
	student_id INT NOT NULL,
	borrowed_date DATE,
	PRIMARY KEY (book_fk_id , student_id),
	FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
)


-- Item 6

INSERT into library(book_fk_id, student_id, borrowed_date) VALUES
	(	(SELECT book_id FROM book WHERE title = 'Alice In Wonderland') , 
 		(SELECT student_id FROM student WHERE name = 'John'),
	 	'15-02-2022' )

INSERT into library(book_fk_id, student_id, borrowed_date) VALUES
	(	(SELECT book_id FROM book WHERE title = 'To kill a mockingbird') , 
 		(SELECT student_id FROM student WHERE name = 'Bob'),
	 	'03-03-2021' ),
	(	(SELECT book_id FROM book WHERE title = 'Alice In Wonderland') , 
 		(SELECT student_id FROM student WHERE name = 'Lera'),
	 	'23-05-2021' ),
	(	(SELECT book_id FROM book WHERE title = 'Harry Potter') , 
 		(SELECT student_id FROM student WHERE name = 'Bob'),
	 	'12-08-2021' )


-- Item 7

-- Item 7.1

SELECT *
FROM library


-- Item 7.2

SELECT s.name , b.title
FROM student s
JOIN library l
ON s.student_id = l.student_id
JOIN book b
ON l.book_fk_id = b.book_id


--Item 7.3

SELECT AVG(s.age)
FROM student s
JOIN library l
ON s.student_id = l.student_id
JOIN book b
ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland'


-- Item 7.4 -- The record in the junction table associated to the deleted student was deleted as well.

DELETE FROM student
WHERE student_id = 2
