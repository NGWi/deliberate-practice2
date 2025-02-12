SELECT DISTINCT p.project_name
FROM projects p
JOIN employee_project ep ON p.project_id = ep.project_id
JOIN employees e ON ep.employee_id = e.employee_id
WHERE e.employee_id = (
    SELECT employee_id 
    FROM employees 
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 1
)