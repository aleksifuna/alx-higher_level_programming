-- creates the table unique_id on the server
-- if the table already exists the script will not fail

CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
