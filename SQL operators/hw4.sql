SELECT 
    department, 
    COUNT(*) AS employee_count, 
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
WHERE status = 'Active' -- Filters rows before aggregation
GROUP BY department
HAVING AVG(salary) > 50000 -- Filters groups after aggregation
ORDER BY avg_salary DESC;
