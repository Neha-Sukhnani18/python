-- 1. VIEW ALL DATA: See all details in the database
SELECT * FROM Team;

-- 2. FILTER & MATCH: Find specific teams starting with 'M' that have over 40 wins
SELECT TeamName, Wins 
FROM Team 
WHERE Wins > 40 
  AND TeamName LIKE 'M%';

-- 3. AGGREGATE DATA: Calculate the lowest and highest points scored across all teams
SELECT 
    MIN(PointsScored) AS LowestPoints, 
    MAX(PointsScored) AS HighestPoints 
FROM Team;
