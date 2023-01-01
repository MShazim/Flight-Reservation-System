-- Creating a schema of Flight Reservation System 

create database FRS 

-- Selecting the Database

use FRS

--Creating table Of Passengers

create table Passenger 
(
    Passenger_id int primary key not null identity (1,1),
    F_Name varchar(20) not null,
    L_Name varchar(20) not null,
    Email varchar(30),
    DOB date not null,
    PassportNo bigint,
    Gender varchar(10) check(Gender in ('Male','Female')),
    MobileNo bigint not null,
    [Address] varchar(100), 
)

--Creating table of Flight

create table Flight
(
    Flight_id int primary key not null identity (100,1),
    FlightName varchar(20) not null,
    Dep_time varchar(10) not null,
    Arr_time varchar(10) not null,
    Seats_available int not null,
    Source varchar(20) not null,
    Destination varchar(20) not null,
    [Date] date not null,
)

-- Creating table of Ticket

create table Ticket
(
    Ticket_id int primary key not null identity (200,1),
    Source varchar(20) not null,
    Destination varchar(20) not null,
)

-- Creating table of Class

create table Class 
(
    Class_id int primary key not null,
    Class_Type varchar(10) not null,
    Fare int not null
)

-- Creating table of FlightType

create table FlightType 
(
    FlightType_id int primary key not null,
    Type varchar(20) check(Type in ('Domestic','International'))
)

--Creating table of Airline

create table Airline
(
    Airline_id int primary key not null,
    Airline_Name varchar(30) not null,
    Contact int not null,
    Email varchar(30)
)

--altering Airline table 

alter table Airline
drop column Contact

alter table Airline
add Contact varchar(30);

--adding foreing key in Flight

alter table Flight
add Airline_id int FOREIGN key REFERENCES Airline(Airline_id)

alter table Flight
add FlightType_id int foreign key REFERENCES FlightType(FlightType_id)

--adding column in Ticket

alter table Ticket
add PassportNo varchar(50)

alter table Ticket 
add F_Name varchar(30)

alter table Ticket 
add L_Name varchar(30)

alter table Ticket 
add [Day] varchar(30)

alter table Ticket 
add Class varchar(30) check (Class in('Business' , 'Economy'))

alter table Ticket 
add MobileNo varchar(30)

--altering table passenger to add age 

alter table passenger
add Age as (CAST(CONVERT(char(8),GETDATE(),112)As int)-CAST(CONVERT(char(8),DOB,112)as int))/10000;



-- Inserting Values in Flight Type 

Insert Into FlightType(FlightType_id,[Type])
Values (501,'Domestic')

Insert Into FlightType(FlightType_id,[Type])
Values (502,'International')

-- Inserting Values in Class

Insert Into Class(Class_id,Class_Type,Fare)
Values (401,'Business',25000)

Insert Into Class(Class_id,Class_Type,Fare)
Values (402,'Economy',10000)

--Inserting data into Airline

INSERT INTO Airline (Airline_id, Airline_Name, Email, Contact) 
VALUES (901, 'Delta', 'info@delta.com', '555-555-1212');

INSERT INTO Airline (Airline_id, Airline_Name, Email, Contact) 
VALUES (902, 'American', 'customer_service@american.com', '555-555-2323');

INSERT INTO Airline (Airline_id, Airline_Name, Email, Contact) 
VALUES (903, 'United', 'support@united.com', '555-555-3434');

INSERT INTO Airline (Airline_id, Airline_Name, Email, Contact) 
VALUES (904, 'Southwest', 'contact@southwest.com', '555-555-4545');

INSERT INTO Airline (Airline_id, Airline_Name, Email, Contact) 
VALUES (905, 'JetBlue', 'customer_service@jetblue.com', '555-555-5656');

--Inserting data in Flight

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('Delta 123', '7:00 AM', '9:00 AM', 100, 'New York', 'Chicago', '2022-01-01', 901, 501);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('American 456', '8:00 AM', '10:00 AM', 80, 'Los Angeles', 'UAE', '2022-01-01', 902, 502);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('United 789', '9:00 AM', '11:00 AM', 60, 'Miami', 'Qatar', '2022-01-01', 903, 502);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('Southwest 159', '10:00 AM', '12:00 PM', 40, 'Boston', 'San Francisco', '2022-01-01', 904, 501);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('JetBlue 357', '11:00 AM', '1:00 PM', 20, 'Seattle', 'New York', '2022-01-01', 905, 501);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('Delta 456', '12:00 PM', '2:00 PM', 100, 'Chicago', 'New York', '2022-01-01', 901, 501);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('American 123', '1:00 PM', '3:00 PM', 80, 'UAE', 'Los Angeles', '2022-01-01', 902, 502);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('United 159', '2:00 PM', '4:00 PM', 60, 'Qatar', 'Miami', '2022-01-01', 903, 502);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('Southwest 789', '3:00 PM', '5:00 PM', 40, 'San Francisco', 'Boston', '2022-01-01', 904, 501);

INSERT INTO Flight (FlightName, Dep_time, Arr_time, Seats_available, Source, Destination, Date, Airline_id, FlightType_id) 
VALUES ('JetBlue 123', '4:00 PM', '6:00 PM', 20, 'New York', 'Seattle', '2022-01-01', 905, 501);

-- creating a table of Place and inserting data in it 

create table Places
(
    Place_id int PRIMARY KEY NOT NULL,
    PlaceName VARCHAR(50) NOT NULL
)

INSERT INTO Places (Place_id, PlaceName) 
VALUES (601, 'New York');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (602, 'Los Angeles');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (603, 'Miami');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (604, 'Boston');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (605, 'Seattle');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (606, 'Chicago');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (607, 'UAE');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (608, 'Qatar');

INSERT INTO Places (Place_id, PlaceName) 
VALUES (609, 'San Francisco');


-- Adding columns in Passenger 

alter table Passenger
add Source varchar(30)

alter table Passenger
add Destination varchar(30)

alter table Passenger
add Class varchar(30) check (Class in('Business' , 'Economy'))

alter table Passenger
add [Day] varchar(20)

ALTER table Passenger
add PassportNo varchar(50) not null

ALTER table Passenger
add MobileNo varchar(50) not null


--checking tables 

select * from Class 
select * from Flight 
select * from Airline
select * from FlightType
select * from Passenger
select * from Ticket
select * from Places 

