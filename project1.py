
import sqlite3
import mysql.connector
#type python3 /Users/yingchen/Desktop/classes/cpsc408/project1/408_Project1/project1.py in terminal to run this code
#somehow won't run in atom
mydb = mysql.connector.connect(host="localhost",
user="root",
password="QQahq34580733~",
auth_plugin='mysql_native_password',database="RideShare")
print(mydb)



mycursor = mydb.cursor()

mycursor.execute('''
CREATE TABLE IF NOT EXISTS User(
    userID INT UNSIGNED PRIMARY KEY,
    findDriver BOOLEAN,
    userRating FLOAT,
    pickupLocation VARCHAR(150),
    dropoffLocation VARCHAR(150),
    PRIMARY KEY(userID)
);
''')

#mycursor.execute("INSERT INTO User VALUES (2,0,3.5,'haha','hahaha');")
#mydb.commit()

mycursor.execute('''
CREATE TABLE IF NOT EXISTS Driver(
    driverID INT UNSIGNED PRIMARY KEY,
    isInDriveMode BOOLEAN,
    currentRating FLOAT,
    userID INTEGER UNSIGNED,
    FOREIGN KEY (userID) REFERENCES User(userID)

);
''')

mycursor.execute("INSERT INTO Driver VALUES (2,0,3.5,2);")
mydb.commit()


mydb.close()
