-- employees                             projects
-- +---------------+---------+           +---------------+---------+
-- | id            | int     |<----+  +->| id            | int     |
-- | first_name    | varchar |     |  |  | title         | varchar |
-- | last_name     | varchar |     |  |  | start_date    | date    |
-- | salary        | int     |     |  |  | end_date      | date    |
-- | department_id | int     |--+  |  |  | budget        | int     |
-- +---------------+---------+  |  |  |  +---------------+---------+
--                              |  |  |
-- departments                  |  |  |  employees_projects
-- +---------------+---------+  |  |  |  +---------------+---------+
-- | id            | int     |<-+  |  +--| project_id    | int     |
-- | name          | varchar |     +-----| employee_id   | int     |
-- +---------------+---------+           +---------------+---------+


BEGIN TRANSACTION;
-- Create the tables
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    salary INT,
    department_id INT REFERENCES departments(id)
);

CREATE TABLE projects (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    start_date DATE,
    end_date DATE,
    budget INT
);

CREATE TABLE employees_projects (
    project_id INT REFERENCES projects(id),
    employee_id INT REFERENCES employees(id),
    PRIMARY KEY (project_id, employee_id)
);
SAVEPOINT created_tables;

-- Insert test data
INSERT INTO departments VALUES 
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Sales'),
(4, 'HR'),         -- This will have no employees
(5, 'Finance'), 
(6, 'Ministry of Funny Walks');   

INSERT INTO employees VALUES
(1, 'John', 'Doe', 70000, 1),
(2, 'Jane', 'Smith', 65000, 1),
(3, 'Bob', 'Johnson', 60000, 2),
(4, 'Alice', 'Williams', 62000, 2),
(5, 'Charlie', 'Brown', 55000, 3),
(6, 'Frank', 'Wilson', 75000, 5),
(7, 'Sarah', 'Miller', 72000, 5),
(8, 'Mike', 'Davis', 68000, 4),   -- No projects assigned yet.
(9, 'Monty', 'Python', 70000, 6); -- Department of Funny Walks

INSERT INTO projects VALUES
(1, 'Project A', '2023-01-01', '2023-12-31', 100000),
(2, 'Project B', '2023-02-01', '2023-11-30', 80000),
(3, 'Project C', '2023-03-01', '2023-10-31', 120000),
(4, 'Project D', '2023-04-01', '2023-09-30', 90000),
(5, 'Project E', '2023-05-01', '2023-08-31', 110000),
(6, 'Project F', '2023-06-01', '2023-12-31', 95000),
(7, 'Project G', '2023-07-01', '2023-12-31', 85000),
(8, 'Project H', '2023-08-01', '2023-12-31', 120000),  -- Tied with for first in Marketing with Project C
(9, 'Project I', '2023-09-01', '2023-12-31', 90000),   -- Tied with with Project D in Marketing
(10,'Project J', '2023-10-01', '2023-12-31', 90000),   -- Tied with with Project D and I in Marketing and Engineering.
-- Funny Walks projects (3 tied for first)
(11, 'Project K', '2023-01-01', '2023-12-31', 120000),
(12, 'Project L', '2023-02-01', '2023-11-30', 120000),
(13, 'Project M', '2023-03-01', '2023-10-31', 120000),
(14, 'Project N', '2023-04-01', '2023-09-30', 90000);


INSERT INTO employees_projects VALUES
(1, 1), (2, 1), (3, 1), (9, 1), -- John works on 4 projects
(1, 2), (2, 2), (10, 2),        -- Jane works on 3 projects
(3, 3), (4, 3), (8, 3),         -- Bob works on 3 projects
(4, 4), (5, 4),                 -- Alice works on 2 projects
(5, 5),                         -- Charlie works on 1 project
(6, 6), (7, 6),                 -- Frank works on 2 projects
(6, 7),                         -- Sarah works on 1 project
(11, 9), (12, 9), (13, 9);      -- Monty works on 4 projects
SAVEPOINT inserted_test_data;


-- Problem: Write a query that retrieves the top 3 projects by budget for each department.

-- A #1)
-- Basic solution that arbitrarily picks third place in case of a tie.
SELECT 
    departments.name AS department, 
    department_projects.title AS project, 
    department_projects.budget
FROM departments
CROSS JOIN LATERAL (
    SELECT DISTINCT projects.title, budget
    FROM employees
    JOIN employees_projects ON employees_projects.employee_id = employees.id
    JOIN projects ON employees_projects.project_id = projects.id
    WHERE department_id = departments.id
    ORDER BY budget DESC
    LIMIT 3
) AS department_projects
ORDER BY departments.name, budget DESC;

-- A #2)
-- Solution using DENSE_RANK() window function that keeps all tied-for-third. Will include second place even if there are 3+ at first place.
WITH ranked AS (
  SELECT DISTINCT
    departments.name AS department, 
    projects.title AS project, 
    projects.budget,
    DENSE_RANK() OVER (PARTITION BY departments.id ORDER BY projects.budget DESC) as budget_rank
  FROM departments
  JOIN employees ON departments.id = employees.department_id
  JOIN employees_projects ON employees.id = employees_projects.employee_id
  JOIN projects ON employees_projects.project_id = projects.id
),
top_two AS (
  -- Get count of projects in ranks 1-2 for each department
  SELECT department, COUNT(*) AS projects_in_top_2
  FROM ranked
  WHERE budget_rank <= 2
  GROUP BY department
)
SELECT ranked.department AS department, 
       ranked.project AS project, 
       ranked.budget
FROM ranked
JOIN top_two ON ranked.department = top_two.department
WHERE ranked.budget_rank <= 2  -- Always include ranks 1 and 2
   OR (ranked.budget_rank = 3 AND top_two.projects_in_top_2 < 3)  -- Include ALL rank 3 if needed
ORDER BY ranked.department, ranked.budget DESC, ranked.project;

-- A #3)
-- More complex query, which stops at 3 total or if we have 3+ tied.
WITH RankedProjects AS (
  SELECT DISTINCT
    departments.name AS department_name, 
    projects.title AS project_title, 
    projects.budget,
    DENSE_RANK() OVER (PARTITION BY departments.id ORDER BY projects.budget DESC) as budget_rank,
    COUNT(*) OVER (PARTITION BY departments.id, projects.budget) as tied_at_this_budget
  FROM departments
  JOIN employees ON departments.id = employees.department_id
  JOIN employees_projects ON employees.id = employees_projects.employee_id
  JOIN projects ON employees_projects.project_id = projects.id
)
SELECT ranked.department_name AS department, 
       ranked.project_title AS project, 
       ranked.budget
FROM RankedProjects ranked
WHERE 
  -- Include rank 1 projects
  ranked.budget_rank = 1
  -- For ranks 2 and 3, only include if the previous rank(s) didn't already give us 3 or more projects
  OR (ranked.budget_rank = 2 AND 
      (
      SELECT COUNT(*) 
      FROM RankedProjects r2 
      WHERE r2.department_name = ranked.department_name 
        AND r2.budget_rank = 1
      ) < 3)
  OR (ranked.budget_rank = 3 AND 
      (
      SELECT COUNT(*) 
      FROM RankedProjects r3 
      WHERE r3.department_name = ranked.department_name 
        AND r3.budget_rank <= 2
      ) < 3)
ORDER BY ranked.department_name, ranked.budget DESC, ranked.project_title;

ROLLBACK;