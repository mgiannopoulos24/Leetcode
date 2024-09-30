-- Find the user with the greatest number of movie ratings
(SELECT 
    u.name AS results
FROM 
    Users u
JOIN 
    MovieRating mr ON u.user_id = mr.user_id
GROUP BY 
    u.user_id, u.name
ORDER BY 
    COUNT(*) DESC, u.name ASC
LIMIT 1)

UNION ALL

-- Find the movie with the highest average rating in February 2020
(SELECT 
    m.title AS results
FROM 
    Movies m
JOIN 
    MovieRating mr ON m.movie_id = mr.movie_id
WHERE 
    mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY 
    m.movie_id, m.title
ORDER BY 
    AVG(mr.rating) DESC, m.title ASC
LIMIT 1);
