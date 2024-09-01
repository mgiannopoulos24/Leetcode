WITH Consecutive AS (
    SELECT 
        s1.id AS id1, s1.visit_date AS date1, s1.people AS people1,
        s2.id AS id2, s2.visit_date AS date2, s2.people AS people2,
        s3.id AS id3, s3.visit_date AS date3, s3.people AS people3
    FROM Stadium s1
    JOIN Stadium s2 ON s1.id = s2.id - 1
    JOIN Stadium s3 ON s2.id = s3.id - 1
    WHERE s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100
)
SELECT DISTINCT s.id, s.visit_date, s.people
FROM Stadium s
JOIN Consecutive c ON s.id IN (c.id1, c.id2, c.id3)
ORDER BY s.visit_date;
