-- Write your query below
SELECT name 
FROM customers 
WHERE name NOT IN (SELECT name
FROM customers INNER JOIN orders 
ON customers.id=orders.customer_id)
