-- creates database hbtn_0d_usa and table states in that db
-- if db and table already exists it will not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL,
	name VARCHAR(256)
	);
