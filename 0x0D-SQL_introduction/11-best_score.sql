-- lists all records with score >= 10 from second_table
-- results should be ordered by score in ascending order
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
