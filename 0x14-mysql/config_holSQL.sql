-- Script that prepares a MySQL server for the project
-- Create a MySQL user named holberton_user on both web-01 and web-02 with
-- the host name set to localhost and the password projectcorrection280hbtn.
-- This will allow us to access the replication status on both servers.
GRANT ALL ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id INT,
       	name VARCHAR(256),
	PRIMARY KEY (id));
INSERT INTO nexus6 VALUES (1, 'Leon')
