#! /usr/bin/python3

import psycopg2 as dbconn

# Open a DB connection
connection = dbconn.connect(dbname = 'postgres', user = 'postgres', password = 'root123', host = '35.228.237.141')

# Open a database cursor
cursor = connection.cursor()

# SQL statement to get db version
print('PostgreSQL database version')
cursor.execute('SELECT version()')
db_version = cursor.fetchone()
print(db_version)

# SQL statement to create a table
#sqlCreateTable = "CREATE TABLE city1(id int, name varchar(128));"
# Execute create table command
#cursor.execute(sqlCreateTable)
# Insert statements
#sqlInsertRow1 = "INSERT INTO city1 values(1, 'NewDelhi')"
#sqlInsertRow2  = "INSERT INTO city1 values(2, 'Srirangam')"
# Insert statement
#cursor.execute(sqlInsertRow1);
#cursor.execute(sqlInsertRow2);
# Select statement
sqlSelect = "SELECT * FROM city1"
cursor.execute(sqlSelect);
rows = cursor.fetchall();
# Print rows
for row in rows:
    print(row);

connection.commit()
cursor.close()
connection.close()
