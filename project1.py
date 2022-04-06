
import sqlite3
import mysql.connector
#type python3 /Users/yingchen/Desktop/classes/cpsc408/project1/408_Project1/project1.py in terminal to run this code
#somehow won't run in atom
mydb = mysql.connector.connect(host="localhost",
user="root",
password="QQahq34580733~",
auth_plugin='mysql_native_password',database="RideShare")
print(mydb)

#Creating the DB:


mydb.close()

create_query = '''
CREATE TABLE IF NOT EXISTS User(
    userID INT, --odd number as ID
    findDriver BOOLEAN,
    userRating FLOAT,
    pickupLocation VARCHAR(150),
    dropoffLocation VARCHAR(150),
    PRIMARY KEY(userID)
);
'''
