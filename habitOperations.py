#import libraries
import sqlite3
import pygame
import datetime
from rectangleButtonClass import inputBox
def addHabit(habitName, habitTime, currentUser):
    #sets initial variables
    failed = None
    timeValid = True
    #ensures the enterd time is a digit not text (validation)
    for i in range(0, len(habitTime)):
        if habitTime[i].isdigit():
            pass
        else:
            timeValid = False
    #if time is an integer and no values are empty...       
    if timeValid and habitTime is not None and habitName is not None and float(habitTime) % 1 == 0 and int(habitTime) < 300:
    #connects to database and sets to correct data types
        habitTime = int(habitTime)
        conn = sqlite3.connect("projectDatabase.db", timeout=30)
        cursor = conn.cursor()
        #finds the date today to set it
        x = datetime.datetime.now()
        today = x.strftime("%x")
        # validation to ensure the users input is positive
        if int(habitTime) > 0:
            #if inputs are correct then add the habit to db
            cursor.execute("INSERT INTO habits(habitName, username, dailyTime, timeLeft, lastCompleted, completed) VALUES (?, ?, ?, ?, ?, ?)",
                   (habitName, currentUser, habitTime, habitTime, today, False))
            #save + close db
            conn.commit()
            conn.close()
            #returns confirmation message
            failed = "addAlertWorked"
            return currentUser, failed
        else:
            #if users input is incorrect then return a message
            failed = "addAlertError"
            return currentUser, failed
    else:
        #if these inputs are invalid then return alert message
        failed = "addAlertError"
        return currentUser, failed
    
def deleteHabit(habitDeleteID, currentUser):
    #connects to database
    conn = sqlite3.connect('projectDatabase.db')
    cursor = conn.cursor()
    #removes habit from db
    cursor.execute("DELETE FROM habits WHERE habitID = ?", (habitDeleteID,))
    #save and close db
    conn.commit()
    conn.close()
    #returns confirmation message
    failed = "deleteSuccess"
    return currentUser, failed

def editHabit(habitEditID, newTime, newName, currentUser):
    #sets initial variables
    failed = None
    timeValid = True
    #validation to ensure time value is a number
    for i in range(0, len(newTime)):
        if newTime[i].isdigit():
            pass
        else:
            timeValid = False
    #connects to database
    conn = sqlite3.connect('projectDatabase.db')
    cursor = conn.cursor()
    #ensures input is a positive integer (validation)
    if timeValid and float(newTime) %1 == 0 and int(newTime) > 1:
        #if inputs are correct then update the habit
        cursor.execute("UPDATE habits SET habitName = ?, dailyTime = ? WHERE habitID = ?", (newName, newTime, habitEditID))
        #save and close db
        conn.commit()
        conn.close()
        #returns confirmation message for successful attempt
        failed = "editSuccess"
        return currentUser, failed
    else:
        #returns confirmation message for failed attempt
        failed = "editFail"
        return currentUser, failed

def logHabit(habitID, timeSpent, user):
    timeValid = True
    for i in range(0, len(timeSpent)):
        if timeSpent[i].isdigit():
            pass
        else:
            timeValid = False
    if timeSpent is not None and timeValid and float(timeSpent) % 1 == 0 and int(timeSpent) >= 1 and int(timeSpent) < 300:
        #connects to database
        conn = sqlite3.connect('projectDatabase.db')
        cursor = conn.cursor()
        #takes the date today
        x = datetime.datetime.now()
        day = x.strftime("%x")
        #selects the habit to be updated and fetches the time
        cursor.execute("SELECT timeLeft FROM habits WHERE habitID = ?", (habitID,))
        #saves the time in variable
        dailyCurrentTime = cursor.fetchone()[0]
        #finds the time difference to be saved again
        newTime = int(dailyCurrentTime) - int(timeSpent)
        #if they havent completed full time period then save it anyway
        if newTime > 0:
            cursor.execute("UPDATE habits SET timeLeft = ? WHERE habitID = ?", (newTime, habitID))
            conn.commit()
            #if they have fully completed update and change completed to true
        else:
            cursor.execute("UPDATE habits SET timeLeft = ?, completed = ?, lastCompleted = ? WHERE habitID = ?", (0, True, day, habitID))
            conn.commit()
        #finds current currency and updaes it with the time spent
        cursor.execute("SELECT currency FROM users WHERE username = ?", (user,))
        userCurrency = int(cursor.fetchone()[0])
        userCurrency = userCurrency + (int(timeSpent) * 7)
        cursor.execute("UPDATE users SET currency = ? WHERE username = ?", (userCurrency, user))
        #save + close db
        conn.commit()
        conn.close()
        #confirmation message for success
        failed = "logSuccess"
        return user, failed
    else:
        #confirmation of failure for invalid inputs
        failed = "logFail"
        return user, failed