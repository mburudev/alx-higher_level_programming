-- Create database
DROP DATABASE IF EXISTS hbtn_test_db_15;
CREATE DATABASE IF NOT EXISTS hbtn_test_db_15;
USE hbtn_test_db_15;

-- Create table
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Create records
INSERT INTO second_table (id, name, score) VALUES (1, "A", 12);
INSERT INTO second_table (id, name, score) VALUES (2, "B", -2);
INSERT INTO second_table (id, name, score) VALUES (3, "C", 12);
INSERT INTO second_table (id, name, score) VALUES (4, "D", 89);
INSERT INTO second_table (id, name, score) VALUES (6, "F", 89);
INSERT INTO second_table (id, name, score) VALUES (7, "G", 89);
INSERT INTO second_table (id, name, score) VALUES (9, "I", 89);
