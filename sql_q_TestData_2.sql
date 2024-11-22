BEGIN TRANSACTION;

-- First, create the tables
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
(1, 'Engineering'),  -- Will have 3 tied for first
(2, 'Marketing'),    -- Will have 2 tied for first, 1 second
(3, 'Sales'),        -- Will have 4 tied for first (showing we stop at 3)
(4, 'Finance');      -- Normal case: 1 first, 1 second, 2 tied for third

INSERT INTO employees VALUES
(1, 'John', 'Doe', 70000, 1),
(2, 'Jane', 'Smith', 65000, 1),
(3, 'Bob', 'Johnson', 60000, 2),
(4, 'Alice', 'Williams', 62000, 2),
(5, 'Charlie', 'Brown', 55000, 3),
(6, 'Frank', 'Wilson', 75000, 3),
(7, 'Sarah', 'Miller', 72000, 4),
(8, 'Mike', 'Davis', 68000, 4);

INSERT INTO projects VALUES
-- Engineering projects (3 tied for first at 120000)
(1, 'Project A', '2023-01-01', '2023-12-31', 120000),
(2, 'Project B', '2023-02-01', '2023-11-30', 120000),
(3, 'Project C', '2023-03-01', '2023-10-31', 120000),
(4, 'Project D', '2023-04-01', '2023-09-30', 90000),

-- Marketing projects (2 tied for first at 110000, 1 second at 100000)
(5, 'Project E', '2023-05-01', '2023-08-31', 110000),
(6, 'Project F', '2023-06-01', '2023-12-31', 110000),
(7, 'Project G', '2023-07-01', '2023-12-31', 100000),
(8, 'Project H', '2023-08-01', '2023-12-31', 90000),

-- Sales projects (4 tied for first at 100000)
(9, 'Project I', '2023-09-01', '2023-12-31', 100000),
(10, 'Project J', '2023-10-01', '2023-12-31', 100000),
(11, 'Project K', '2023-11-01', '2023-12-31', 100000),
(12, 'Project L', '2023-12-01', '2023-12-31', 100000),
(17, 'Project Q', '2023-12-01', '2023-12-31', 50000),

-- Finance projects (normal case)
(13, 'Project M', '2023-01-01', '2023-12-31', 130000),
(14, 'Project N', '2023-02-01', '2023-11-30', 110000),
(15, 'Project O', '2023-03-01', '2023-10-31', 90000),
(16, 'Project P', '2023-04-01', '2023-09-30', 90000);

INSERT INTO employees_projects VALUES
-- Engineering assignments
(1, 1), (2, 1), (3, 1),         -- John works on all three 120000 projects
(1, 2), (4, 2),                 -- Jane works on one 120000 and one 90000

-- Marketing assignments
(5, 3), (6, 3), (7, 3),         -- Bob works on both 110000 and the 100000
(6, 4), (8, 4),                 -- Alice works on one 110000 and the 90000

-- Sales assignments
(9, 5), (10, 5),                -- Charlie works on two 100000
(11, 6), (12, 6),               -- Frank works on two other 100000

-- Finance assignments
(13, 7), (14, 7),               -- Sarah works on 130000 and 110000
(15, 8), (16, 8);               -- Mike works on both 90000
SAVEPOINT inserted_test_data;

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
SAVEPOINT ranked_query;


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
SAVEPOINT three_part_query;


ROLLBACK;
