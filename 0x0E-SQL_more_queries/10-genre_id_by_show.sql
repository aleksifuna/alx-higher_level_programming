-- lists all shows contained in the db

SELECT s.title, g.genre_id FROM tv_shows s
RIGHT JOIN tv_show_genres g
ON s.id=g.show_id
ORDER BY s.title, g.genre_id ASC;
