import sqlite3

database = 'xy'

conn = sqlite3.connect(database)
print('opened data successfully')

#read SQL query for getting all the tables of database into a dataframe
import pandas as pd
tables = pd.read_sql("""SELECT*
FROM NOBEL_WINZ
WHERE SUBJECT NOT LIKE'P%';
;""",conn)
tables

#read table from the database into dataframe
matches = pd.read_sql("""SELECT*
FROM NOBEL_WINZ
WHERE SUBJECT NOT LIKE'P%';
;""",conn)

#print table info
matches.info()