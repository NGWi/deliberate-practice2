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
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Sales'),
(4, 'HR'),         -- This will have no employees
(5, 'Finance');    

INSERT INTO employees VALUES
(1, 'John', 'Doe', 70000, 1),
(2, 'Jane', 'Smith', 65000, 1),
(3, 'Bob', 'Johnson', 60000, 2),
(4, 'Alice', 'Williams', 62000, 2),
(5, 'Charlie', 'Brown', 55000, 3),
(6, 'Frank', 'Wilson', 75000, 5),
(7, 'Sarah', 'Miller', 72000, 5);

INSERT INTO projects VALUES
(1, 'Project A', '2023-01-01', '2023-12-31', 100000),
(2, 'Project B', '2023-02-01', '2023-11-30', 80000),
(3, 'Project C', '2023-03-01', '2023-10-31', 120000),
(4, 'Project D', '2023-04-01', '2023-09-30', 90000),
(5, 'Project E', '2023-05-01', '2023-08-31', 110000),
(6, 'Project F', '2023-06-01', '2023-12-31', 95000),
(7, 'Project G', '2023-07-01', '2023-12-31', 85000);

INSERT INTO employees_projects VALUES
(1, 1), (2, 1), (3, 1),  -- John works on 3 projects
(1, 2), (2, 2),          -- Jane works on 2 projects
(3, 3), (4, 3),          -- Bob works on 2 projects
(4, 4), (5, 4),          -- Alice works on 2 projects
(5, 5),                  -- Charlie works on 1 project
(6, 6), (7, 6),          -- Frank works on 2 projects
(6, 7);                  -- Sarah works on 1 project
SAVEPOINT inserted_test_data;

SELECT departments.name, department_projects.title, department_projects.budget
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

ROLLBACK;