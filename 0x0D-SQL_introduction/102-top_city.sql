-- 19. Temperatures #1
-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
