CREATE TABLE IF NOT EXISTS Salesman(
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT
    Comission REAL 
);

INSERT INTO Salesman (Salesman_id, name, city, Comission)VALUES
('5001','James Hoog', 'new york',0.15),
('5002','nail knite','paris',0.13),
('5005','pit alex','london',0.11),
('5006','mc lyon','paris',0.14),
('5007','paul adam', 'rome',0.13),
('5003','lauson hen','san jose',0.12);

SELECT* FROM Salesman;
CREATE TABLE IF NOT EXISTS Orders(
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date,customer_id,Salesman_id) VALUES
('5001','James Hoog', 'new york',0.15),
('5002','nail knite','paris',0.13),
('5005','pit alex','london',0.11),
('5006','mc lyon','paris',0.14),
('5007','paul adam', 'rome',0.13),
('5003','lauson hen','san jose',0.12);
SELECT * FROM Orders;
SELECT name, comission
FROM Salesman;