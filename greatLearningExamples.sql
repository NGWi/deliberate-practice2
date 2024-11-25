/*
Find treatments with the price higher than the average for their type. Display two columns:

the name of the treatment,
the type of the treatment.
*/

WITH avg_prices AS (
    SELECT type, AVG(price) as avg_price
    FROM treatment
    GROUP BY type
)
SELECT treatment.name, treatment.type
FROM treatment
JOIN avg_prices 
    ON treatment.type = avg_prices.type
WHERE treatment.price > avg_prices.avg_price
ORDER BY treatment.type, treatment.name;

/*
Your task
Find books that have been borrowed from the library as many times or more than the most frequently borrowed book written by author Stephen King. Display one column only:

the title of the book.
Make sure to include each book only once. Order the results alphabetically by book titles.
*/

WITH sk_borrowed AS (
    SELECT book.id, COUNT(*) as borrow_count
    FROM book_loan
    JOIN book ON book.id = book_loan.book_id
    JOIN author ON book.author_id = author.id
    WHERE author.first_name = 'Stephen' 
        AND author.last_name = 'King'
    GROUP BY book.id
),
max_sk AS (
    SELECT MAX(borrow_count) as max_borrowed
    FROM sk_borrowed
)
SELECT DISTINCT book.title
FROM book
JOIN book_loan ON book.id = book_loan.book_id
GROUP BY book.id, book.title
HAVING COUNT(*) >= (SELECT max_borrowed FROM max_sk)
ORDER BY book.title;

/*
For every employee, display their reporting hierarchy, starting from the top-most authority, the "head boss," down to the employee. Select five columns:

the employee's ID; label it id,
the first name of the employee,
the last name of the employee,
the ID of their immediate manager, label it manager_id,
the hierarchical path from the head boss to the employee, label it path.
Construct the path as detailed below:

For the employee who does not have a manager, indicate 'Boss' in the path column.
For all other employees, depict the hierarchy from the boss to the employee, starting with 'Boss->', followed by the last name of their immediate subordinate, then the last name of that subordinate's subordinate, and so on, until you reach the last name of the employee in question. Use the '->' sign to separate the last names of the managers.
For example, the final result for employee Allen Garcia should look like this:

Boss->Green->Garcia
*/

WITH RECURSIVE hierarchy AS (
    SELECT
        id,
        first_name,
        last_name,
        manager_id,
        'Boss' AS path
    FROM employee
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        next.id,
        next.first_name,
        next.last_name,
        next.manager_id,
        CONCAT(hierarchy.path, '->', next.last_name) -- MySQL
    FROM employee next
    JOIN hierarchy ON next.manager_id = hierarchy.id
)
SELECT 
    id,
    first_name,
    last_name,
    manager_id,
    path
FROM hierarchy
;