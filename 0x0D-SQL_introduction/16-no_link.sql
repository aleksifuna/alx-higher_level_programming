-- lists all records of the table second_table
-- rows without name value are excluded
-- records are listed by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
