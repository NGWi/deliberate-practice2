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


-- Write a query that retrieves the top 3 projects by budget for each department.

-- Solution with window function in CTE, will return more than 3 if there are any ties.
WITH RankedProjects AS (
  SELECT 
    d.name as department_name,
    p.title as project_title,
    p.budget,
    DENSE_RANK() OVER (PARTITION BY d.id ORDER BY p.budget DESC) as budget_rank
  FROM departments d
  JOIN employees e ON e.department_id = d.id -- Note, plain JOIN means INNER JOIN
  JOIN employees_projects ep ON ep.employee_id = e.id
  JOIN projects p ON p.id = ep.project_id
)
SELECT 
  department_name,
  project_title,
  budget
FROM RankedProjects
WHERE budget_rank <= 3
ORDER BY department_name, budget DESC;

-- Solution with different function in CTE, will arbitrarily select which is 3rd if there are ties
WITH RankedProjects AS (
  SELECT 
    d.name as department_name,
    p.title as project_title,
    p.budget,
    ROW_NUMBER() OVER (PARTITION BY d.id ORDER BY p.budget DESC) as budget_rank
  FROM departments d
  JOIN employees e ON e.department_id = d.id
  JOIN employees_projects ep ON ep.employee_id = e.id
  JOIN projects p ON p.id = ep.project_id
)
SELECT 
  department_name,
  project_title,
  budget
FROM RankedProjects
WHERE budget_rank <= 3
ORDER BY department_name, budget DESC;

-- Solution with RANK() - only includes extras if they tie for 3rd place
WITH RankedProjects AS (
  SELECT 
    d.name as department_name,
    p.title as project_title,
    p.budget,
    RANK() OVER (PARTITION BY d.id ORDER BY p.budget DESC) as budget_rank
  FROM departments d
  JOIN employees e ON e.department_id = d.id
  JOIN employees_projects ep ON ep.employee_id = e.id
  JOIN projects p ON p.id = ep.project_id
)
SELECT 
  department_name,
  project_title,
  budget
FROM RankedProjects
WHERE budget_rank <= 3
ORDER BY department_name, budget DESC;

-- Solution for MySQL 5.7 and earlier using variables. Similiar to ROW_NUMBER() solution above.
SELECT department_name, project_title, budget
FROM (
  SELECT 
    department_name,
    project_title,
    budget,
    @rank := IF(@current_department = department_name, @rank + 1, 1) AS budget_rank,
    @current_department := department_name
  FROM (
    SELECT 
      d.name as department_name,
      p.title as project_title,
      p.budget
    FROM departments d
    JOIN employees e ON e.department_id = d.id
    JOIN employees_projects ep ON ep.employee_id = e.id
    JOIN projects p ON p.id = ep.project_id
    ORDER BY d.name, p.budget DESC
  ) ranked_projects
  CROSS JOIN (SELECT @rank := 0, @current_department := '') vars -- We could have used a regular JOIN here, but CROSS JOIN is commonly used in MySQL variable initialization patterns because it makes the intent clear - we want to combine every row with our initialization row
) ranked
WHERE budget_rank <= 3;

-- Solution using correlated subquery approach. Similiar to ROW_NUMBER() solution above.
SELECT 
    d.name as department_name,
    p.title as project_title,
    p.budget
FROM departments d
JOIN employees e ON e.department_id = d.id
JOIN employees_projects ep ON ep.employee_id = e.id
JOIN projects p ON p.id = ep.project_id
WHERE p.id IN (
    SELECT p2.id
    FROM departments d2
    JOIN employees e2 ON e2.department_id = d2.id
    JOIN employees_projects ep2 ON ep2.employee_id = e2.id
    JOIN projects p2 ON p2.id = ep2.project_id
    WHERE d2.id = d.id
    ORDER BY p2.budget DESC
    LIMIT 3
)
ORDER BY department_name, budget DESC;

-- Solution using correlated subquery approach that handles ties (similar to RANK()) O(n^2)
SELECT 
    d.name as department_name,
    p.title as project_title,
    p.budget
FROM departments d
JOIN employees e ON e.department_id = d.id
JOIN employees_projects ep ON ep.employee_id = e.id
JOIN projects p ON p.id = ep.project_id
WHERE (
    SELECT COUNT(DISTINCT p2.budget)
    FROM departments d2
    JOIN employees e2 ON e2.department_id = d2.id
    JOIN employees_projects ep2 ON ep2.employee_id = e2.id
    JOIN projects p2 ON p2.id = ep2.project_id
    WHERE d2.id = d.id
    AND p2.budget > p.budget
) < 3
ORDER BY department_name, budget DESC;

/* How it works:
   1. For each project, counts how many DISTINCT budgets are higher in its department
   2. If fewer than 3 distinct higher budgets exist, includes the project
   3. This means if multiple projects tie for 1st, 2nd, or 3rd place, all are included
   4. Similar to RANK() because it leaves gaps after ties
*/

-- More efficient solution without window functions
WITH ProjectRanks AS (
  SELECT 
    d.id as dept_id,
    d.name as department_name,
    p.budget,
    COUNT(DISTINCT p2.budget) as higher_budgets
  FROM departments d
  JOIN employees e ON e.department_id = d.id
  JOIN employees_projects ep ON ep.employee_id = e.id
  JOIN projects p ON p.id = ep.project_id
  LEFT JOIN employees e2 ON e2.department_id = d.id
  LEFT JOIN employees_projects ep2 ON ep2.employee_id = e2.id
  LEFT JOIN projects p2 ON p2.id = ep2.project_id 
    AND p2.budget > p.budget
  GROUP BY d.id, d.name, p.id, p.budget
  HAVING COUNT(DISTINCT p2.budget) < 3
)
SELECT 
  pr.department_name,
  p.title as project_title,
  p.budget
FROM ProjectRanks pr
JOIN employees e ON e.department_id = pr.dept_id
JOIN employees_projects ep ON ep.employee_id = e.id
JOIN projects p ON p.id = ep.project_id AND p.budget = pr.budget
ORDER BY department_name, budget DESC;

/* How it works:
   1. Pre-calculates ranks by counting higher budgets in a single GROUP BY
   2. Uses LEFT JOINs to count higher budgets
   3. Only needs one pass through the data
   4. More efficient than correlated subquery for large datasets
   5. Still handles ties like RANK()
*/

-- Without using aliases:
WITH ProjectRanks AS (
  SELECT 
    departments.id AS department_id,
    departments.name AS department_name,
    projects.budget,
    COUNT(DISTINCT higher_projects.budget) AS higher_budgets
  FROM departments
  JOIN employees            ON departments.id = employees.department_id
  JOIN employees_projects   ON employees.id = employees_projects.employee_id
  JOIN projects             ON employees_projects.project_id = projects.id
  LEFT JOIN employees higher_employees             ON departments.id = higher_employees.department_id
  LEFT JOIN employees_projects higher_emp_projects ON higher_employees.id = higher_emp_projects.employee_id
  LEFT JOIN projects higher_projects               ON higher_emp_projects.project_id = higher_projects.id 
    AND higher_projects.budget > projects.budget
  GROUP BY departments.id, departments.name, projects.id, projects.budget
  HAVING COUNT(DISTINCT higher_projects.budget) < 3
)
SELECT
  ProjectRanks.department_name,
  projects.title AS project_title,
  projects.budget
FROM ProjectRanks
JOIN employees          ON ProjectRanks.department_id = employees.department_id
JOIN employees_projects ON employees.id = employees_projects.employee_id
JOIN projects           ON employees_projects.project_id = projects.id
  AND projects.budget = ProjectRanks.budget
ORDER BY department_name, budget DESC;

-- More efficient solution that sorts first O(n log n). Handles tied for third in O(n log n) like DENSE_RANK()
WITH OrderedProjects AS (
  SELECT 
    departments.id AS department_id,
    departments.name AS department_name,
    projects.id AS project_id,
    projects.title AS project_title,
    projects.budget
  FROM departments
  JOIN employees            ON departments.id = employees.department_id
  JOIN employees_projects   ON employees.id = employees_projects.employee_id
  JOIN projects            ON employees_projects.project_id = projects.id
  ORDER BY departments.id, projects.budget DESC
),
RankedProjects AS (
  SELECT 
    current_project.department_id,
    current_project.department_name,
    current_project.project_id,
    current_project.project_title,
    current_project.budget,
    COUNT(DISTINCT higher_budget_project.budget) AS higher_budgets
  FROM OrderedProjects current_project
  LEFT JOIN OrderedProjects higher_budget_project
    ON current_project.department_id = higher_budget_project.department_id 
    AND higher_budget_project.budget > current_project.budget
  GROUP BY 
    current_project.department_id, 
    current_project.department_name,
    current_project.project_id,
    current_project.project_title,
    current_project.budget
)
SELECT 
  department_name,
  project_title,
  budget
FROM RankedProjects
WHERE higher_budgets < 3
ORDER BY department_name, budget DESC;

/* How it works:
   1. First CTE (OrderedProjects) sorts the data by department and budget - O(n log n)
   2. Second CTE (RankedProjects) compares each project with higher-budget projects in same department
   3. More efficient than previous version because we're working with sorted data
   4. Still handles ties like RANK()
   5. Cleaner code with self-documenting table aliases
*/

-- Most efficient basic solution using running count of distinct values
WITH OrderedProjects AS (
  SELECT 
    departments.id AS department_id,
    departments.name AS department_name,
    projects.id AS project_id,
    projects.title AS project_title,
    projects.budget,
    COUNT(DISTINCT projects.budget) OVER (
      PARTITION BY departments.id 
      ORDER BY projects.budget DESC
      ROWS UNBOUNDED PRECEDING
    ) - 1 AS higher_distinct_budgets  -- subtract 1 to exclude current budget
  FROM departments
  JOIN employees            ON departments.id = employees.department_id
  JOIN employees_projects   ON employees.id = employees_projects.employee_id
  JOIN projects            ON employees_projects.project_id = projects.id
)
SELECT 
  department_name,
  project_title,
  budget
FROM OrderedProjects
WHERE higher_distinct_budgets < 3
ORDER BY department_name, budget DESC;

/* How it works:
   1. Sort projects by budget DESC within each department
   2. Use window function to count distinct budgets up to current row
   3. Subtract 1 to exclude current row's budget
   4. Single pass through the sorted data - O(n log n) for the sort
   5. No need for self-joins or multiple counts
   6. Still handles ties correctly
*/

-- Optimized solution that only does joins once
WITH ProjectsByDepartment AS (
  SELECT 
    departments.id AS department_id,
    departments.name AS department_name,
    projects.title AS project_title,
    projects.budget
  FROM departments
  JOIN employees            ON departments.id = employees.department_id
  JOIN employees_projects   ON employees.id = employees_projects.employee_id
  JOIN projects            ON employees_projects.project_id = projects.id
)
SELECT 
  department_name,
  project_title,
  budget
FROM (
  SELECT 
    *,
    ROW_NUMBER() OVER (
      PARTITION BY department_id 
      ORDER BY budget DESC
    ) as budget_rank
  FROM ProjectsByDepartment
) ranked --this alias is never referenced.
WHERE budget_rank <= 3
ORDER BY department_name, budget DESC;

/* How it works:
   1. Do all joins once in the CTE
   2. Use window function to rank within each department
   3. Filter for top 3
   4. Much more efficient than correlated subquery
   5. Note: This version uses ROW_NUMBER() so no ties
   6. Could use RANK() instead if we want to include ties
*/

-- Same solution but using RANK() to handle ties
WITH ProjectsByDepartment AS (
  SELECT 
    departments.id AS department_id,
    departments.name AS department_name,
    projects.title AS project_title,
    projects.budget
  FROM departments
  JOIN employees            ON departments.id = employees.department_id
  JOIN employees_projects   ON employees.id = employees_projects.employee_id
  JOIN projects             ON employees_projects.project_id = projects.id
)
SELECT 
  department_name,
  project_title,
  budget
FROM (
  SELECT 
    *,
    RANK() OVER (
      PARTITION BY department_id 
      ORDER BY budget DESC
    ) as budget_rank
  FROM ProjectsByDepartment
) ranked --this alias is never referenced.
WHERE budget_rank <= 3
ORDER BY department_name, budget DESC;

-- CROSS JOIN Example
WITH 
colors AS (
  SELECT 'red' as color
  UNION SELECT 'blue'
  UNION SELECT 'green'
),
sizes AS (
  SELECT 'small' as size
  UNION SELECT 'medium'
  UNION SELECT 'large'
)
SELECT * FROM colors CROSS JOIN sizes;

/* Results would be:
color  | size
-------|-------
red    | small
red    | medium
red    | large
blue   | small
blue   | medium
blue   | large
green  | small
green  | medium
green  | large
*/

--Solution like ROW_NUMBER()
SELECT departments.name, department_projects.title, department_projects.budget
FROM departments
CROSS JOIN LATERAL (
    SELECT projects.title, budget
    FROM employees
    JOIN employees_projects ON employees_projects.employee_id = employees.id
    JOIN projects ON employees_projects.project_id = projects.id
    WHERE department_id = departments.id
    ORDER BY budget DESC
    LIMIT 3
) AS department_projects
ORDER BY departments.name;

-- Final solution using DENSE_RANK() window function
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
  SELECT department, COUNT(*) as projects_in_top_2
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
