import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="QQahq34580733~", auth_plugin='mysql_native_password')
print(mydb)
mydb.close()
