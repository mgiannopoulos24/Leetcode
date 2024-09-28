SELECT 
    s1.id, 
    CASE
        WHEN s1.id % 2 = 1 AND s2.id IS NOT NULL THEN s2.student
        WHEN s1.id % 2 = 0 THEN s2.student
        ELSE s1.student
    END AS student
FROM Seat s1
LEFT JOIN Seat s2 ON 
    (s1.id % 2 = 1 AND s1.id + 1 = s2.id) -- For odd IDs, join with next even ID
    OR (s1.id % 2 = 0 AND s1.id - 1 = s2.id) -- For even IDs, join with previous odd ID
ORDER BY s1.id;
