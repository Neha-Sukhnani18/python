--connect with sqlite database
--import necessary libraries
import sqlite3

database = 'database.sqlite'

conn = dqlite3.connect(database)
print('opened data successfully')

--read sql query for getting all the tables of database into a dataframe
import pandas as pd 
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type ='table';""",conn)
tables

--read table from the database into dataframe
matches = pd.read_sql("""SELECT * FROM Match;""",conn)
matches head.()
"""**Conclusion-**
-12 Numeric features (integer and numeric) and 1 categorical feature(text) 
- 3 columns with null VALUES
"""

-- get the average win margin of all the winning teams for season 9
result1=pd.read_sql("""SELECT AVG(Win_Margin),Match_Winner FROM Match WHERE Season_Id == 9 GROUP BY Match_Winner ORDER BY AVG(Win_Margin);""",conn)
result1

--get the count of the venues for season 9
result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id) FROM Match WHERE Season_Id == 9;""",conn)

result2 
--get the minimum, maximum and average Win Margin
--also get the total number of players who have received man of the match throughout all the seasons

result3 = pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_match FROM Match;""",conn)
result3

--return total of win_margins for all the winners in season 9
result4 = pd.read_sql("""SELECT SM(Win_Margin) FROM Match WHERE Season_Id == 9;""",conn)
reult4
