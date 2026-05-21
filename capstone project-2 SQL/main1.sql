--create restaurant table
CREATE TABLE IF NOT EXISTS Restaurant(
    name TEXT,
    neighborhood TEXT,
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT

);

--INSERT DATA
INSERT INTO Restaurant(name,neighborhood, cuisine, review, price, health)
values
    ('peter','brooklyn','steak','4.4','$$$$','A'),
    ('jongro','midtown','korean','3.5','$$','A'),
    ('pocha','midtown','pizza','4.0','$$$','A'),
    ('lighthouse','queens','chinese','3.9','$','A'),
    ('minca','downtown','american','4.6','$$$',''),
    ('marea','chinatown','chinese','3.0','$$',''),
    ('dirty candy','uptown','italian','4.9','$$$$','B'),
    ('di fara pizza','brooklyn','pizza','3.8','$$','A'),
    ('golden unicorn','uptown','italian','3.8','$$','A');

--1) distinct neighborhoods
SELECT DISTINCT neighborhood
FROM Restaurant;

--2) distinct cuisine types
SELECT DISTINCT cuisine 
FROM Restaurant;

--3)chinese takeout options
SELECT*
FROM Restaurant
WHERE Restaurant
WHERE cuisine = 'Chinese';
--4)Restaurants with reviews 4 and above
SELECT*
FROM Restaurant 
WHERE review >=4.0;

--5)italian restaurants with $$ to $$$ 
SELECT *
FROM Restaurants
WHERE cuisine = 'italian'
    AND price IN ('$$','$$$');

--6) restaurants with exactly $$$
SELECT*
FROM Restaurant
WHERE price = '$$$';

777) restaurants name contains "candy"
SELECT *
FROM Restaurant
WHERE name LIKE '%Candy%';

--8)restaurants in midtown, downtown or chinatown
SELECT*
FROM Restaurant 
WHERE neighborhood IN ('midtown','downtown','chinatown');

--9)health grade pending(empty value)
SELECT*
FROM Restaurant
WHERE health='' OR health IS NULL;

--10) TOP 4 RESTAURANTS BASED ON REVIEWS
SELECT*
FROM Restaurant
ORDER BY review DESC
LIMIT 4;