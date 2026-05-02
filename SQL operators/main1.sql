--create the student table if it does not exist
-- NOT NULL is used for name to ensure every student record has a name
CREATE TABLE IF NOT EXISTS STUDENT(
    ROLL_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);
--Insert sample data into the student table
INSERT INTO STUDENT (ROLL_NO, NAME, ADDRESS, PHONE,AGE)VALUES
('1','RAM','DELHI','*****',18),
('2','RAMESH','GURGAON','*****',18),
('3','SUJIT','ROHTAK','*****',20),
('4','SURESH','DELHI','*****',18),
('5','HARSH','GURGAON','*****',18);

--Select all records from the student table to verify insertion
SELECT * FROM STUDENT;
--Query students who are 18 years old and live in delhi
SELECT * FROM STUDENT WHERE AGE=18 AND ADDRESS='DELHI';
--Query students who are 18 years old and named ram
SELECT * FROM STUDENT WHERE AGE = 18 AND NAME ='RAM';
--Query students named RAM or sujit
SELECT * FROM STUDENT WHERE NAME = 'RAM' OR AGE=20;
--query students aged 18 and named ram or ramesh
SELECT * FROM STUDENT WHERE AGE = 18 AND (NAME= 'RAM' OR NAME='RAMESH');
