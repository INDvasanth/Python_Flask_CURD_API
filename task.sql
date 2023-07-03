
create table users
(id int not null auto_increment, 
deal_date date, 
sec_code int not null,
sec_name varchar(30),
client_name varchar(50),
deal_type varchar(1) not null,
qty int,
price float,
primary key(id));

insert into users(deal_date, sec_code, sec_name, client_name, deal_type, qty, price) 
values('2023-06-30', 542580, "AARTECH", "VEENA RAJESH SHAH", 'S', 56000, 103.55);


select * from users;