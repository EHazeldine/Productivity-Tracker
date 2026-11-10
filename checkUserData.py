import sqlite3
def checkLogIn(usernameEntered, passwordEntered):
    #if the text entered by the user is empty then return back to the log in page
    if usernameEntered == "" or passwordEntered == "":
        print("space is empty")
        return "logIn", None
    else:
    #connects to the database
        conn = sqlite3.connect("projectDatabase.db")
        cursor = conn.cursor()
    #checks that there is a record of this username and password
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                   (usernameEntered, passwordEntered))
    #if there is a record, it was successful
        if cursor.fetchone():
            failed = False
            return "main Page", usernameEntered
        else:
    #if there was no record then reject it and recursively handle
            failed = True
            return "logIn", usernameEntered, failed
        
def checkSignUp(newUsernameEntered, newPasswordEntered):
    newCurrency = 0
    #Connects to the database
    conn = sqlite3.connect("projectDatabase.db")
    cursor = conn.cursor()
    #Checks if the username is taken
    cursor.execute("SELECT * FROM users WHERE username = ?",
                   (newUsernameEntered, ))
    #if taken it will recusively handle this until a new username is inputted
    if cursor.fetchone():
        failed = "nameError"
        return "signUp", None, failed
    else:
        #Checks length of the password entered, ensuring it is not too short/long
        if len(newPasswordEntered) > 7 and len(newPasswordEntered) < 20:
            #Adds a new instance of a username and password using pysqlite3
            cursor.execute("INSERT INTO users (username, password, currency) VALUES (?, ?, ?)",
                           (newUsernameEntered, newPasswordEntered, newCurrency))
            #Saves new changes
            conn.commit()
            return "main Page", newUsernameEntered
        else:
            failed = "rangeError"
            #If the password is out of range, outputs a message and recursively handles this
            return "signUp", None, failed