-- This is test data to be loaded into a mariadb docker container

DROP DATABASE IF EXISTS game_store_employee_db;
CREATE DATABSE IF NOT EXISTS game_store_employee_db;
USE game_store_employee_db;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS employees,
                     departments,
                     dept_manager,
                     dept_employee,
                     titles,
                     salaries;


CREATE TABLE employees (
    employee_no INT PRIMARY KEY AUTO_INCREMENT,
    birth_date DATE NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    gender ENUM ('M','F','Non-Binary') NOT NULL,
    hire_date DATE NOT NULL
);

CREATE TABLE departments (
    dept_no CHAR(4) NOT NULL PRIMARY KEY,
    dept_name VARCHAR(40) NOT NULL UNIQUE KEY
);

CREATE TABLE dept_manager (

);

CREATE TABLE dept_employee (

);

CREATE TABLE titles (

);

CREATE TABLE salaries (

);