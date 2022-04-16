
import sqlite3
import mysql.connector
#type python3 /Users/yingchen/Desktop/classes/cpsc408/project1/408_Project1/project1.py in terminal to run this code
#somehow won't run in atom
mydb = mysql.connector.connect(host="localhost",
user="root",
password="QQahq34580733~",
auth_plugin='mysql_native_password',database="RideShare")
print(mydb)

# Functions
def print_user_info(user_data):
    print("User pickup location: " + user_data[0][0])
    print("User dropoff location location: " + user_data[0][1])
    print("User star rating: " + str(user_data[0][2]))

def update_drive_mode(role, shouldBeInDriveMode):
    turn_drivemode_on = ("UPDATE Driver SET isInDriveMode="+ str(shouldBeInDriveMode) + " WHERE driverID=" + str(role))
    mycursor.execute(turn_drivemode_on)
    mydb.commit()

def driver_exit():
    print("have a good day, bye driver")
    update_drive_mode(role, 0)
    exit(1)


# Functions end



mycursor = mydb.cursor()

role = input("what's your ID?")
role = int(role)
#if ID is odd then user, even then driver
print(role)

#user case
if role%2 != 0: #user is odd number
    print("this is a user")
    pickupLocation = input("enter your pick up location")
    dropoffLocation = input("enter your drop off location")
#driver case
else: #driver is even number
    print("this is a driver")
    SQLcommand = ('''SELECT isInDriveMode FROM Driver WHERE driverID =''' + str(role))
    mycursor.execute(SQLcommand)
    #print out the driver mode
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    if myresult[0][0]==0: #driver is not ready to drive
       on_off = input("do you want to turn the drive mode on or not?(y/n)")
       if on_off == 'n':
            driver_exit()
       else: #driver is turning the drive mode on
            update_drive_mode(role, 1)

    print("driver can drive")
    print("start matching with user") #match with a random user who has findDriver boolean set to true
    #print(myresult[0][0])
    #update the driver table to turn the drivemode on
          # turn_drivemode_on = ("UPDATE Driver SET isInDriveMode=1 WHERE driverID=" + str(role))

    matchUser = ("SELECT userID FROM User WHERE findDriver = 1")
    # matchUser = ("SELECT * FROM User")
    mycursor.execute(matchUser)

    myresult = mycursor.fetchall()
    user_id = myresult[0][0]
    print(user_id) #print out userID that get matched with a driver
    match_user_info = ("SELECT pickupLocation,dropoffLocation,userRating FROM User WHERE userID=" + str(user_id))
    mycursor.execute(match_user_info)
    myresult = mycursor.fetchall()
    print()
    print(myresult) #print out the user's drop off and pick up locations and the rating from this specific UserID
    print_user_info(myresult)
    #prompt driver see if they want to accept the user
    decision = input("do you want to drive this user? enter y for yes, and n for no")
    if decision == 'n': #driver not accepting request
        driver_exit()




    update_drive_mode(role, 0)












mydb.close()
