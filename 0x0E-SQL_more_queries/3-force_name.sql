-- creates the table force_name on MySQL server
-- if it already exists the script will not fail

CREATE TABLE IF NOT EXISTS force_name(
	id INT DEFAULT 1,
	name VARCHAR(256) NOT NULL
	)
