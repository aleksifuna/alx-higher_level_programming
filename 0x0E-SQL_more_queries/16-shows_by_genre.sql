-- lists all shows and genres linked to the show

SELECT s.title, g.name FROM tv_shows s
LEFT JOIN tv_show_genres t
ON s.id = t.show_id
LEFT JOIN tv_genres g
ON g.id = t.genre_id
ORDER BY s.title, g.name;
