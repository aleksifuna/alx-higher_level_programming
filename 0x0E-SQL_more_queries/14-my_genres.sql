-- lists all genres of the show 'Dexter'

SELECT g.name FROM tv_genres g
INNER JOIN tv_show_genres t
ON g.id = t.genre_id
INNER JOIN tv_shows s
ON t.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
