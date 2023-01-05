-- prepare a MySQL server for this project
-- create user with privileges on one database

CREATE database IF NOT EXISTS hbnb_dev_db;
CREATE user IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performace_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
