#imports libraries
import sqlite3
def resetNewDay(currentUsername):
    #sets initial list of habits and associated times
    IDList = []
    timeList = []
    #connects to the database
    conn = sqlite3.connect('projectDatabase.db')
    cursor = conn.cursor()
    #selects all habitIDs and daily times associated to the user and saves it to a list
    cursor.execute("SELECT habitID, dailyTime FROM habits WHERE username = ?", (currentUsername, ))
    fullList = cursor.fetchall()
    #fetches all completede values associated to the user and saves to another list
    cursor.execute("SELECT completed FROM habits WHERE username = ?", (currentUsername, ))
    completedList = cursor.fetchall()
    complete = 1
    #fetches the streak length and stores it in a variable
    cursor.execute("SELECT streakLength FROM users WHERE username = ?", (currentUsername, ))
    streak = cursor.fetchone()[0]
    #sets index for a for loop
    index = (len(fullList) - 1)
    #for each habit, add all IDs to one array and all times to another
    for i in range(len(fullList)):
        IDList.append(fullList[i][0])
        timeList.append(fullList[i][1])
        #checks if any completed values are false
        if completedList[i][0] != 1:
            complete = 0
    #if all completed values are true then increment streak length
    if complete == 1:
        cursor.execute("UPDATE users SET streakLength = ? WHERE username = ?", ((streak + 1), currentUsername, ))
    #if not then reset the streak length to zero
    else:
        cursor.execute("UPDATE users SET streakLength = ? WHERE username = ?", (0, currentUsername, ))
    #for each habit...
    for x in range (0, len(IDList)):
        #set completed to false and timeleft to the daily time value, resetting both for a new day
        cursor.execute("UPDATE habits SET completed = ? WHERE habitID = ?", (0, IDList[x] ))
        cursor.execute("UPDATE habits SET timeLeft = ? WHERE habitID = ?", (timeList[x], IDList[x] ))
    #saves and closes all operations to the database
    conn.commit()
    conn.close()