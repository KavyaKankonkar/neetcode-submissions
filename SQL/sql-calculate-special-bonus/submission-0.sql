-- Write your query below
SELECT employee_id ,salary*0 AS Bonus 
FROM employees
WHERE name LIKE 'M%' OR employee_id%2 =0  

UNION ALL

SELECT employee_id ,salary AS bonus
FROM employees
WHERE name NOT LIKE 'M%' AND employee_id%2 <>0  

order by employee_id
