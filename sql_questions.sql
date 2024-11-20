-- https://coderpad.io/blog/coding-challenges/tiny-interview-sql-challenge/
-- Tiny Interview #5
-- CodinGamers database diagram

-- You are working on a competitive programming website, where users can solve problems in several languages.

-- The database has the schema pictured above. Every time a player submits their code, it creates a row in the submissions table with the score of their attempt between 0 and 100.

-- Write MySQL queries to retrieve the following results. The expected answer is provided for each one so you can check that your queries are correct.

-- 1. The number of submissions per language.
-- +----------+------------+
-- | language | lang_count |
-- +----------+------------+
-- | C++      |       1197 |
-- | Haskell  |       1345 |
-- | C        |       1101 |
-- | Ruby     |        956 |
-- | Python   |       1275 |
-- | Java     |       1078 |
-- | C#       |       1120 |
-- +----------+------------+
-- 2. Players who are exactly 25 years old.
-- +------------+
-- | nickname   |
-- +------------+
-- | trictrac   |
-- | MSmits     |
-- | cup_of_tea |
-- | Scipi0     |
-- +------------+
-- 3. The top 10 users ranked by number of unique problems attempted.
-- +-------------+--------------------+
-- | nickname    | problems_attempted |
-- +-------------+--------------------+
-- | kiwijam     |                 99 |
-- | k4ng0u      |                 99 |
-- | R4N4R4M4    |                 96 |
-- | Seti        |                 95 |
-- | Bob         |                 92 |
-- | daaskare    |                 92 |
-- | jacek       |                 91 |
-- | Xyze        |                 90 |
-- | TylerDurden |                 90 |
-- | Petras      |                 90 |
-- +-------------+--------------------+
-- 4. Players who submitted on the same problem with at least two different languages.
-- +----------+
-- | nickname |
-- +----------+
-- | dbdr     |
-- | Fluxor   |
-- | Marchete |
-- | nmahoude |
-- | SlyB     |
-- | Wld      |
-- +----------+
-- 5. Players who solved at least 60 different MEDIUM or HARD problems with a 100% score.
-- +-------------+
-- | nickname    |
-- +-------------+
-- | R4N4R4M4    |
-- | darkhorse64 |
-- | reCurse     |
-- | DaFish      |
-- | kiwijam     |
-- | Xyze        |
-- +-------------+
SELECT language, count(language) AS lang_count
FROM submissions
GROUP BY language
;

-- Had to troubleshoot for Q #2 because expected answer set was out of date, as above.
SELECT nickname, birth, TIMESTAMPDIFF(YEAR, birth, CURDATE())
FROM players
WHERE nickname in ("trictrac", "MSmits", "cup_of_tea", "Scipi0")
;
SELECT nickname
FROM players
WHERE TIMESTAMPDIFF(YEAR, birth, "2022-8-21") = 25
;

SELECT nickname, COUNT(DISTINCT problem_id) AS problems_attempted
FROM players
INNER JOIN submissions
  ON players.user_id = submissions.user_id
GROUP BY nickname
ORDER BY problems_attempted DESC
LIMIT 10
;
-- Q 4 A 1
SELECT DISTINCT nickname
FROM players 
INNER JOIN submissions
  ON players.user_id = submissions.user_id
GROUP BY nickname, problem_id
HAVING COUNT(DISTINCT language) >= 2
;
-- A 2, unnecessarily compicated.
SELECT nickname
FROM players 
INNER JOIN (
  SELECT user_id
  FROM submissions
  GROUP BY user_id, problem_id
  HAVING COUNT(DISTINCT language) >= 2
) AS temp
ON players.user_id = temp.user_id
GROUP BY nickname
;

SELECT nickname
FROM players
INNER JOIN submissions
  ON players.user_id = submissions.user_id
INNER JOIN problems
  ON submissions.problem_id = problems.problem_id
WHERE difficulty in ("medium", "hard") AND score = 100
GROUP BY nickname
HAVING COUNT(DISTINCT submissions.problem_id) >= 60

-- https://neetcode.io/problems/sql-default-values
-- Default Values
-- Table columns can have default values. When inserting rows into a table it's possible to omit values for some columns. The database will automatically insert NULL for those columns, unless a default value is specified. You can specify a default value for a column when creating a table.

-- CREATE TABLE users (
--     name TEXT DEFAULT 'Anonymous',
--     email TEXT,
--     age INTEGER DEFAULT 18
-- );
-- In the above example, the name column has a default value of 'Anonymous', and the age column has a default value of 18. The email column does not have a default value, so it will be NULL if no value is provided.

-- You can specify a default value by using the DEFAULT keyword followed by the value you want to set.

-- To 'drop' a column, means to remove it from the table.
-- Challenge
-- Create a table called videos with the following columns:

-- id of type INTEGER with no default value
-- name of type TEXT with a default value of 'Untitled'
-- is_published of type BOOLEAN with a default value of false
BEGIN TRANSACTION;
CREATE TABLE videos (
    id INTEGER,
    name TEXT DEFAULT 'Untitled',
    is_published BOOLEAN DEFAULT false
)
;
SAVEPOINT created_table;

-- The below section will cause the wrong answer to be returned, but is probably a better practice in real life.
CREATE OR REPLACE FUNCTION set_default_id()
RETURNS TRIGGER AS 
$$
BEGIN
    IF NEW.id IS NULL THEN
        SELECT COALESCE(MAX(id), 0) + 1 INTO NEW.id FROM videos;
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE plpgsql;
CREATE TRIGGER before_insert_videos
BEFORE INSERT ON videos
FOR EACH ROW EXECUTE FUNCTION set_default_id();
SAVEPOINT created_trigger_fuction;
-- End better practice section --

-- Do not modify below this line --
INSERT INTO videos (id, name, is_published) 
VALUES (1, 'My Video', true),
       (2, 'Another Video', false);

INSERT INTO videos (id)
VALUES (3),
       (4);

INSERT INTO videos (name)
VALUES ('Video with no ID');

SELECT * FROM videos;
ROLLBACK;