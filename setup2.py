import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="QQahq34580733~", auth_plugin='mysql_native_password')
print(mydb)
# create cursor obj to interact with mySQL
mycursor = mydb.cursor()
# create the DB
mycursor.execute("CREATE SCHEMA RideShare;")
# show the databases that exist in my local mySQL
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
mydb.close()
