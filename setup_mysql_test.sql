-- prepare a test user for MySQL in project

-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create new user
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';

-- grant user all privileges
GRANT ALL PRIVILEGES
    ON hbnb_test_db.*
    TO 'hbnb_test'@'localhost';

-- grant select privileges to user
GRANT SELECT
    ON performace_schema.*
    TO 'hbnb_test'@'localhost';

-- commit changes to user
FLUSH PRIVILEGES;
