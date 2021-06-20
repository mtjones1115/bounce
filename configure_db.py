import mysql.connector

## Configure databases

mydb = mysql.connector.connect(
  host= config.host,
  user= config.user,
  password= config.password,
  database= config.database
)