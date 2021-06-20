import mysql.connector
import config

## Configure databases

mydb = mysql.connector.connect(
  host= config.host,
  user= config.user,
  password= config.password,
  database= config.database
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)