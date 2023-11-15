-- lists all cities in the db with the states

SELECT c.id, c.name, s.name FROM cities c
INNER JOIN states s ON
c.state_id = s.id
ORDER BY c.id ASC;
