
import sqlite3
import mysql.connector
import time
#type python3 /Users/yingchen/Desktop/classes/cpsc408/project1/408_Project1/project1.py in terminal to run this code
#somehow won't run in atom
mydb = mysql.connector.connect(host="localhost",
user="root",
password="QQahq34580733~",
auth_plugin='mysql_native_password',database="RideShare")
autocommit=True#https://stackoverflow.com/questions/9305669/mysql-python-connection-does-not-see-changes-to-database-made-on-another-connect
print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#  print(x)

 #mycursor.execute("USE RideShare")

# Functions
def print_user_info(user_data):
    print("User pickup location: " + user_data[0][0])
    print("User dropoff location location: " + user_data[0][1])
    print("User star rating: " + str(user_data[0][2]))

def update_drive_mode_user_or_driver(role, shouldBeInDriveMode):
    if(role %2 == 0):#Driver
        turn_drivemode_on = ("UPDATE Driver SET isInDriveMode="+ str(shouldBeInDriveMode) + " WHERE driverID=" + str(role))
    else:#User
        turn_drivemode_on = ("UPDATE User SET findDriver="+ str(shouldBeInDriveMode) + " WHERE userID=" + str(role))
    mycursor.execute(turn_drivemode_on)
    mydb.commit()

def driver_exit():
    print("have a good day, bye driver")
    # update_drive_mode_user_or_driver(role, 0)
    exit(1)

def is_user_matched_with_driver(userID): #returns True if is matched, returns False if not matched
    #Fetch all rows where the userID is contained within a driver
    SQLcommand = ('''SELECT driverID FROM Driver WHERE userID =''' + str(userID))
    mycursor.execute(SQLcommand)
    myresult = mycursor.fetchall()

    print("Driver ID: " + str(myresult[0][0]))

    SQLcommand2 = ('''SELECT isInDriveMode FROM Driver WHERE driverID =''' + str(myresult[0][0]))
    mycursor.execute(SQLcommand2)
    myresult2 = mycursor.fetchall()

    print("Drive mode: " + str(myresult2[0][0]))


    if(myresult2[0][0] == 1):
        return True
    else:
        return False
#    if myresult[0][0]=user_id:

    #return
def print_db():
    SQLcommand = ('''SELECT * FROM Driver''')
    mycursor.execute(SQLcommand)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)

    SQLcommand = ('''SELECT * FROM User''')
    mycursor.execute(SQLcommand)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)


# Functions end




role = input("what's your ID?")
role = int(role)
#if ID is odd then user, even then driver
print(role)

#user case
if role%2 != 0: #user is odd number
    print("this is a user")
    pickupLocation_input = input("enter your pick up location")
    dropoffLocation_input = input("enter your drop off location")
    mycursor.execute("UPDATE User SET pickupLocation=\'" + str(pickupLocation_input) + "\' WHERE userID=" + str(role))
    mycursor.execute("UPDATE User SET dropoffLocation=\'" + str(dropoffLocation_input) + "\' WHERE userID=" + str(role))
    mydb.commit()

    #run the user, have them enter location and update the database(database by default set all locations to null), then turn the look for driver mode on then quit
    #run the driver to turn drive mode on
    #run the user and check if the look for driver mode is on and there is one driver has the drive mode on then it's matched


    mycursor.execute("SELECT findDriver FROM User WHERE userID=" + str(role))
    check_userMode = mycursor.fetchall()
    # print(check_userMode)
    mycursor.execute("SELECT isInDriveMode FROM Driver WHERE userID=" + str(role))
    check_driverMode = mycursor.fetchall()
    # print(check_driverMode)

    if check_userMode[0][0] == 0: #user findDriver is 0, so turn it to 1
    #at the beginning, all user's LookForDriver attribute are set to false, so assume no one is looking for driver at the beginning
        update_drive_mode_user_or_driver(role, 1) #update the user findDriver mode to 1
    # look_for_driver_to_true = ('''UPDATE TABLE User SET findDriver = 1 WHERE UserID =''' + str(role))
        print("matching you with a driver now")
        exit(1)


    if check_userMode[0][0] == 1 and is_user_matched_with_driver(role):
        #is_user_matched_with_driver(role)
        print("found a driver for you")
        mycursor.execute("SELECT driverID FROM Driver WHERE userID=" + str(role))
        rideID = mycursor.fetchall()
        #provide the rider with a ride ID
        print("your ride has driver with ID: " + str(rideID[0][0]))
        print("bringing you back to the main menu...")
        time.sleep(2)
        exit(1)


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
            update_drive_mode_user_or_driver(role, 1)


    print("driver can drive")
    print("start matching with user") #match with a random user who has findDriver boolean set to true
    #print(myresult[0][0])
    #update the driver table to turn the drivemode on
          # turn_drivemode_on = ("UPDATE Driver SET isInDriveMode=1 WHERE driverID=" + str(role))

    matchUser = ("SELECT userID FROM User WHERE findDriver = 1")
    # matchUser = ("SELECT * FROM User")
    mycursor.execute(matchUser)

    myresult = mycursor.fetchall()

    if(len(myresult) == 0):
        print("there are no users looking for drivers")
        driver_exit()

    user_id = myresult[0][0]
    print(user_id) #print out userID that get matched with a driver
    mycursor.execute("UPDATE Driver SET userID="+ str(user_id) + " WHERE driverID=" + str(role))
    mydb.commit()
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
    elif decision == 'y': #driver accept the request
        print("driving the user now")
        time.sleep(2)
        print("driver with ID "+ str(role) + " is driving user with ID " + str(user_id))



        #updating the user ID in the driver table
        update_userID = ("UPDATE TABLE Driver SET userID = " + str(user_id))
        # update_drive_mode_user_or_driver(role, 0) #set driver mode to inactive





    # update_drive_mode_user_or_driver(role, 0)












mydb.close()
