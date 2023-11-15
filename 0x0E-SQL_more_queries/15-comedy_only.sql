-- lists all the comedy shows in the dababase

SELECT DISTINCT s.title FROM tv_shows s
INNER JOIN tv_show_genres t
ON s.id = t.show_id
INNER JOIN tv_genres g
ON t.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
