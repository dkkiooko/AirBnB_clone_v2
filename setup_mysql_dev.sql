-- prepare a MySQL server for this project

-- create database
CREATE DATABASE
    IF NOT EXISTS hbnb_dev_db;

-- create user
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

-- grant privileges to user
GRANT ALL PRIVILEGES
    ON hbnb_dev_db.*
    TO 'hbnb_dev'@'localhost';

-- grant select privileges to user
GRANT SELECT
    ON performace_schema.*
    TO 'hbnb_dev'@'localhost';

-- commit privileges to db
FLUSH PRIVILEGES;
