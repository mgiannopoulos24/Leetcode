WITH FirstOrders AS (
    -- Step 1: Find the first order (earliest order_date) for each customer
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
),
ImmediateFirstOrders AS (
    -- Step 2: Join the first orders with the Delivery table to classify the orders
    SELECT d.customer_id,
           (d.order_date = d.customer_pref_delivery_date) AS is_immediate
    FROM Delivery d
    JOIN FirstOrders f
    ON d.customer_id = f.customer_id
    AND d.order_date = f.first_order_date
)
-- Step 3: Calculate the percentage of immediate first orders
SELECT ROUND(100.0 * SUM(is_immediate) / COUNT(*), 2) AS immediate_percentage
FROM ImmediateFirstOrders;
