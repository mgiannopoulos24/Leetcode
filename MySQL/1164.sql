WITH LatestPrice AS (
    SELECT product_id, new_price, change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
),
MaxDate AS (
    SELECT product_id, MAX(change_date) AS last_change_date
    FROM LatestPrice
    GROUP BY product_id
)
SELECT p.product_id, COALESCE(lp.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN MaxDate md ON p.product_id = md.product_id
LEFT JOIN LatestPrice lp 
    ON md.product_id = lp.product_id 
    AND md.last_change_date = lp.change_date;
