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
