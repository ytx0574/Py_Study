drop database if exists awesome;

create databse awesome;

use awesome;

grant select, insert, update, delete, on awesome.* to 'root'@'localhost' identified by 'root';

create table users (
  `id` varchar(50) not null,
  `email` varchar(50) not null,



)