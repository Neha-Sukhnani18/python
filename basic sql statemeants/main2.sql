from google.colab import files
file=files.upload()
import sqlite3

database = 'xy'

conn = sqlite3.connect(database)
print('opened data successfully')

import panadas as pd 
tables = pd.read_sql("""SELECT*
FROM NOBEL_WINZ
WHERE SUBJECT NOT LIKE'P%';
;""",conn)
tables
 teams = pd.read_sql("""SELECT*
FROM NOBEL_WINZ
WHERE SUBJECT NOT LIKE'P%';""",conn)
teams

matches = pd.read_sql("""SELECT*
FROM NOBEL_WINZ
WHERE SUBJECT NOT LIKE'P%';""",conn)

"""**conclusion-** 
 
 matches

MI_wins = pd.read_sql("""SELECT*
FROM NOBEL_WINZ
WHERE SUBJECT NOT LIKE'P%';""",conn)
MI_wins

new_teams = pd.read_sql("""SELECT*
FROM NOBEL_WINZ
WHERE SUBJECT NOT LIKE'P%';""",conn)
new_teams

min_max_margin = pd.read_sql("""SELECT MIN(WIN_Margin),MAX(Win_Margin)FROM Match;""",conn)
min_max_margin
