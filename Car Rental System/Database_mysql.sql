-- drop database database_mysql;
create database database_mysql;
	use database_mysql;

	create table driver(
		License_No int(10) not null primary key,
		Driver_Name varchar(50) not null,
		Age int(2) not null,
		Phone varchar(20) not null,
		Address varchar(70) not null);

	create table car(
		Car_No int(4) not null primary key,
		Car_Type varchar(50) not null,
		Car_Color varchar(50) not null,
		License_No int(10) not null,
		constraint Car_FK foreign key (License_No) references driver(License_No)
		on delete cascade
		on update cascade);

	create table reservation(
		Res_ID int not null auto_increment,
		Book_Time timestamp not null DEFAULT current_timestamp,
		City varchar(80) not null,
		Street varchar(80) not null,
		Destination varchar(80) not null,
		Price varchar(11) not null,
		License_No int(10) not null,
		constraint PK primary key(Res_ID),
		constraint Reservation_FK foreign key (License_No) references driver(License_No)
		on delete cascade
		on update cascade);

	create table customer(
		Email varchar(50) not null primary key,
		Customer_Name varchar(80) not null,
		Phone varchar(20) not null);

	create table customer_reservations(
		Email varchar(50) not null,
		Res_ID int not null,
		constraint Mail_FK foreign key (Email) references customer(Email)
		on delete cascade
		on update cascade,
		constraint ResID_FK foreign key (Res_ID) references reservation(Res_ID)
		on delete cascade
		on update cascade);

	insert into driver (License_No, Driver_Name, Age, Phone, Address) values
		(2011467831, 'Yassen', 33, '1501476314', 'Alex,October'),
		(2014684379, 'Khamis', 32, '1264971348', 'MarsaMatroh'),
		(2015144912, 'Ahmed', 30, '1559782176', 'Alex,SedeGaber'),
		(2016159757, 'Fares', 31, '1546231789', 'Alex,Manshia'),
		(2016247831, 'Mostafa', 37, '1547832196', 'Kafr_Elshikh,Byla'),
		(2017246578, 'Maher', 47, '1247832134', 'Alex,Agamy'),
		(2018246159, 'Adel', 50, '1147832645', 'Alex,Manshia');

	insert into car (Car_No, Car_Type, Car_Color, License_No) values
		(122, 'Hyundai', 'Sliver', 2011467831),
		(159, 'Toyota', 'Red', 2015144912),
		(464, 'Hyundai', 'Sliver', 2015144912),
		(542, 'Hyundai', 'Sliver', 2018246159),
		(3248, 'Ford', 'Yellow', 2016159757),
		(3497, 'Bugatti', 'Gray', 2018246159),
		(9456, 'Chevrolet', 'Red', 2016247831);

	insert into reservation (City, Street, Destination, Price, License_No) values
		('Alex', 'Bitash', 'October', 50, 2011467831),
		('Alex', 'Bahary', 'Mahata', 33, 2015144912),
		('Alex', 'Hanoveel', 'Khairallah', 35, 2014684379),
		('Kafr_Elshikh', 'Hamool', ' Sakha', 100, 2016159757),
		('Alex', 'Asafra', 'Backoos', 40, 2017246578),
		('Alex', 'SedeBichr', 'Somoha', 45, 2018246159),
		('MarsaMatrouh', 'AlexStreet', 'Alexandria', 200, 2015144912);

	insert into customer (Customer_Name, Phone, Email) values
		('Kamal', '01001248677', 'Kamal@gmail.com'),
		('Gaber', '1005468478', 'Gaber@gmail.com'),
		('Fathalla', '1008971246', 'Fathalla@gmail.com'),
		('Khaled', '1215975346', 'Khaled@gmail.com'),
		('Said', '1214679121', 'Said@gmail.com'),
		('Loay', '1134791534', 'Loay@gmail.com'),
		('Pasem', '1064741355', 'Pasem@gmail.com');

	insert into customer_reservations (Email, Res_ID) values
		('Kamal@gmail.com', 1),
		('Gaber@gmail.com', 2),
		('Fathalla@gmail.com', 3),
		('Khaled@gmail.com', 1),
		('Khaled@gmail.com', 4),
		('Said@gmail.com', 5),
		('Loay@gmail.com', 4),
		('Pasem@gmail.com', 6),
		('Fathalla@gmail.com', 7);

-- select * from driver;
-- select * from car;
-- select * from reservation;
-- select * from customer;
-- select * from customer_reservations;
-- SELECT * FROM car WHERE Car_Color LIKE 'Silver';
