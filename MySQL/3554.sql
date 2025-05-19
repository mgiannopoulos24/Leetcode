SELECT
    LEAST(pi1.category, pi2.category) AS category1,
    GREATEST(pi1.category, pi2.category) AS category2,
    COUNT(DISTINCT pp1.user_id) AS customer_count
FROM ProductPurchases pp1
JOIN ProductInfo pi1 ON pp1.product_id = pi1.product_id
JOIN ProductPurchases pp2
JOIN ProductInfo pi2 ON pp2.product_id = pi2.product_id
    AND pi1.category < pi2.category
WHERE pp1.user_id = pp2.user_id
GROUP BY category1, category2
HAVING customer_count >= 3
ORDER BY 
    customer_count DESC,
    category1 ASC,
    category2 ASC;