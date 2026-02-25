
-- 1. Display names and salaries of employees whose salary is > average [cite: 8]
SELECT name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);


-- 2. Retrieve top 5 highest-paid employees [cite: 10]
SELECT * FROM employees 
ORDER BY salary DESC 
LIMIT 5;


-- 3. Calculate total count, average, min, and max salary [cite: 12, 13, 14, 15]
SELECT 
    COUNT(*) AS total_employees, 
    AVG(salary) AS average_salary, 
    MIN(salary) AS min_salary, 
    MAX(salary) AS max_salary 
FROM employees;


-- 4. Total sales per region where total > 50,000 [cite: 17, 18]
SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(amount) > 50000;

-- 5. Number of unique job roles [cite: 19]
SELECT COUNT(DISTINCT job_role) FROM employees;
-- Logic: DISTINCT prevents counting duplicate role titles[cite: 20].

-- 6. Students scoring between 60 and 80 [cite: 21, 22]
SELECT * FROM students WHERE marks BETWEEN 60 AND 80;

-- 7. Employees whose commission is NULL [cite: 30]
SELECT * FROM employees WHERE commission IS NULL;


-- 8. Increase salary of "IT" department by 10% [cite: 32]
UPDATE employees 
SET salary = salary * 1.10 
WHERE department = 'IT';


-- 9. Delete records of students scoring < 40 [cite: 34]
DELETE FROM students WHERE marks < 40;


-- 10. Employees earning more than their department average (No Joins) [cite: 36]
SELECT * FROM e1 
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees e2 
    WHERE e1.department = e2.department
);
