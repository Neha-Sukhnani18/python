
import sqlite3

database = 'xx'

conn = sqlite3.connect(database)
print('opened data successfully')

#read SQL query for getting all the tables of database into a dataframe
#here SELECT * means select all
import pandas as pd
tables = pd.read_sql("""SELECT customer.cust_name,salesman.name,salesman.city
FROM Customer
JOIN Salesman ON Customer.city=Salesman.city;
;""",conn)
