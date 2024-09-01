SELECT 
    t1.id,
    CASE 
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN t2.id IS NOT NULL THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM 
    Tree t1
LEFT JOIN 
    (SELECT DISTINCT p_id AS id FROM Tree WHERE p_id IS NOT NULL) t2
ON t1.id = t2.id;
