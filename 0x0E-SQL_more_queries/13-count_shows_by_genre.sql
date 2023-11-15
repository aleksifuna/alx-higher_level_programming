-- lists all genres from db and number of shows linked to each

SELECT g.name AS genre, COUNT(t.genre_id) AS number_of_shows
FROM tv_genres g
RIGHT JOIN tv_show_genres t
ON g.id = t.genre_id
GROUP BY t.genre_id
ORDER BY number_of_shows DESC;
