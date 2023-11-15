-- creates the MYSQL server user user_0d_1
-- the user should have all the privileges
-- password should be user_0d_1_pwd
-- if the user already exists the code should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
