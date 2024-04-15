import mysql.connector

dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = '1234'
)


# prepare a cursor object


cursorObject = dataBase.cursor()

# create a db

cursorObject.execute('CREATE DATABASE elderco')

print("All Done!")