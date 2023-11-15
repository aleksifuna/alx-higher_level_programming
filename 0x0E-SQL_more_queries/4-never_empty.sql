-- creates the table id_not_null on the server
-- if the table already exists the script will not fail

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
