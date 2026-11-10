#import sqlite3 library, and connect to the database
import sqlite3
conn = sqlite3.connect('projectDatabase.db')
cursor = conn.cursor()

#creates the table that includes information about the users
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL UNIQUE PRIMARY KEY,
    password TEXT NOT NULL,
    currency INTEGER NOT NULL,
    streakLength INTEGER NOT NULL DEFAULT 0,
    lastLoggedIn DATE
    );
               """)

#creates the table storing the habits the users have created
cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
    habitID INTEGER PRIMARY KEY AUTOINCREMENT, 
    habitName TEXT NOT NULL,
    username TEXT NOT NULL,
    dailyTime INTEGER NOT NULL,
    timeLeft INTEGER NOT NULL,
    lastCompleted DATE NOT NULL,
    completed BOOLEAN NOT NULL CHECK (completed IN (0,1)),
    FOREIGN KEY (username) REFERENCES users(username)
    );
                """)
conn.commit()
conn.close()