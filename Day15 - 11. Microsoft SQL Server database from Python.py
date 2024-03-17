

import pyodbc


server = 'LAPTOP-PG47J1NE'
database = 'AdventureWorks2012'

connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Integrated Security=True'


conn = pyodbc.connect(connection_string)


cursor = conn.cursor()



conn = pyodbc.connect(connection_string)


cursor = conn.cursor()



cursor.execute("SELECT * FROM HumanResources.Department")


rows = cursor.fetchall()


for row in rows:
    print(row)

cursor.close()
conn.close()
