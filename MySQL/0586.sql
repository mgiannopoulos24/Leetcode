-- Step 1: Count the number of orders placed by each customer
WITH OrderCounts AS (
    SELECT customer_number, COUNT(*) AS order_count
    FROM Orders
    GROUP BY customer_number
),

-- Step 2: Find the maximum number of orders placed by any customer
MaxOrderCount AS (
    SELECT MAX(order_count) AS max_count
    FROM OrderCounts
)

-- Step 3: Select the customer(s) who have the maximum number of orders
SELECT customer_number
FROM OrderCounts
WHERE order_count = (SELECT max_count FROM MaxOrderCount);
