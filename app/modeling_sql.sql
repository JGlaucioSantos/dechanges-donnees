USE db_glaucio;

#candidate_identification
CREATE TABLE db_glaucio.candidate_identification
(
id int auto_increment,
id_candidate int,
candidate_first_name varchar(100),
candidate_last_name varchar(100),
gender varchar(10),
primary key (id)
);

#candidate_contact
CREATE TABLE db_glaucio.candidate_contact
(
id int auto_increment,
id_candidate int,
candidate_email varchar(100),
phone_number varchar(15),
primary key (id)
);

#candidate_location
CREATE TABLE db_glaucio.candidate_location
(
id int auto_increment,
id_candidate int, 
candidate_address varchar(10),
postal_code varchar(10),
city varchar(20),
country varchar(10),
code_country varchar(6),
primary key (id)
);

#job_information
CREATE TABLE db_glaucio.job_information
(
id int auto_increment,
id_candidate int, 
department varchar(20),
job_title varchar(25),
annual_salary int,
primary key (id)
);

#hiring_process
CREATE TABLE db_glaucio.hiring_process
(
id int auto_increment,
id_candidate int, 
position_type varchar(10),
position_status varchar(10),
poste_date datetime,
hired_Date datetime,
primary key (id)
);


# SELECTs

#candidate_identification
SELECT * FROM db_glaucio.candidate_identification;

#candidate_contact
SELECT * FROM db_glaucio.candidate_contact;

#candidate_location
SELECT * FROM db_glaucio.candidate_location;

#candidate_contact
SELECT * FROM db_glaucio.job_information;

#hiring_process
SELECT * FROM db_glaucio.hiring_process;

