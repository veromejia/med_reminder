-- creates the database db_medreminder and the user user_medreminder
-- create database db_medreminder
CREATE DATABASE IF NOT EXISTS db_medreminder;
-- creates user user_medreminder
CREATE USER IF NOT EXISTS 'user_medreminder'@'localhost' IDENTIFIED BY 'pwd_medreminder';
-- grants select privileges
GRANT ALL PRIVILEGES ON db_medreminder.* TO 'user_medreminder'@'localhost' IDENTIFIED BY 'pwd_medreminder' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'user_medreminder'@'localhost';
FLUSH PRIVILEGES;

USE db_medreminder;

CREATE TABLE IF NOT EXISTS patient(
id INT UNIQUE NOT NULL AUTO_INCREMENT,
name VARCHAR(60) NOT NULL,
last_name VARCHAR(60) NOT NULL,
email VARCHAR(120),
phone varchar(15),
PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS prescription(
id INT UNIQUE NOT NULL AUTO_INCREMENT,
patient_id INT NOT NULL,
medication VARCHAR(120) NOT NULL,
frequency VARCHAR(60) NOT NULL,
start_dt DATETIME NOT NULL,
end_dt DATETIME NOT NULL,
noti_type VARCHAR(60),
PRIMARY KEY(id),
FOREIGN KEY(patient_id) REFERENCES patient(id)
);

CREATE TABLE IF NOT EXISTS task(
id INT UNIQUE NOT NULL AUTO_INCREMENT,
task_command VARCHAR(60) NOT NULL,
task_comment VARCHAR(60) NOT NULL,
last_dt DATETIME NOT NULL,
status VARCHAR(60) NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS task_x_prescription(
task_id INT NOT NULL,
prescription_id INT NOT NULL,
PRIMARY KEY(task_id, prescription_id),
FOREIGN KEY(task_id) REFERENCES task(id),
FOREIGN KEY (prescription_id) REFERENCES prescription(id)
);
