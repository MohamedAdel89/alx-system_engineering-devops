-- Script that prepares a MySQL server for the project
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replicahbtn';
FLUSH PRIVILEGES;
