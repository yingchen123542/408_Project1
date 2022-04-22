import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="QQahq34580733~", auth_plugin='mysql_native_password', database="RideShare")
# # create cursor obj to interact with mySQL
mycursor = mydb.cursor()
# # create the DB
# # show the databases that exist in my local mySQL
mycursor.execute("SHOW DATABASES")
for x in mycursor:
 print(x)




mycursor.execute("USE RideShare;")


#mydb.close()

#
# mycursor = mydb.cursor()
#
#build the database
mycursor.execute('''
CREATE TABLE IF NOT EXISTS User(
    userID INT UNSIGNED PRIMARY KEY,
    findDriver BOOLEAN,
    userRating FLOAT,
    pickupLocation VARCHAR(150),
    dropoffLocation VARCHAR(150)
);
''')

mycursor.execute("INSERT INTO User VALUES (1,0,3.5, '', '');")
mydb.commit()
mycursor.execute("INSERT INTO User VALUES (3,0,3.5, '', '');")
mydb.commit()
mycursor.execute("INSERT INTO User VALUES (5,0,3.5, '', '');")
mydb.commit()
mycursor.execute("INSERT INTO User VALUES (7,0,3.5, '', '');")
mydb.commit()
mycursor.execute("INSERT INTO User VALUES (9,0,3.5, '', '');")
mydb.commit()

#
# print(mycursor.rowcount, "was inserted.")
# mycursor.execute("SELECT * FROM User")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)




mycursor.execute('''
CREATE TABLE IF NOT EXISTS Driver(
    driverID INT UNSIGNED PRIMARY KEY,
    isInDriveMode BOOLEAN,
    currentRating FLOAT,
    userID INTEGER UNSIGNED,
    FOREIGN KEY (userID) REFERENCES User(userID)

);
''')

mycursor.execute("INSERT INTO Driver VALUES (2,0,3.5,NULL);")
mydb.commit()
mycursor.execute("INSERT INTO Driver VALUES (4,0,3.5,NULL);")
mydb.commit()
mycursor.execute("INSERT INTO Driver VALUES (6,0,3.5,NULL);")
mydb.commit()
mycursor.execute("INSERT INTO Driver VALUES (8,0,3.5,NULL);")
mydb.commit()
mycursor.execute("INSERT INTO Driver VALUES (10,0,3.5,NULL);")
mydb.commit()
mycursor.execute("INSERT INTO Driver VALUES (12,0,3.5,NULL);")
mydb.commit()


# print(mycursor.rowcount, "was inserted.")
# mycursor.execute("SELECT * FROM Driver")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)



mydb.close()
