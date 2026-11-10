#imports any libraries and functions made
import pygame
pygame.init()
import sqlite3
import sys
import time
import threading
import datetime
from failureMessage import failure
from failureMessage import runningTime
from rectangleButtonClass import imageRectButton
from rectangleButtonClass import rectButton
from rectangleButtonClass import inputBox
from habitOperations import addHabit
from habitOperations import deleteHabit
from habitOperations import editHabit
from habitOperations import logHabit
from resetDay import resetNewDay

def mainPage(usernameEntered, failed):
    #connects to database
    conn = sqlite3.connect("projectDatabase.db")
    cursor = conn.cursor()
    #fetches the old last logged in date and stores it in lastLoggedIn
    cursor.execute("SELECT lastLoggedIn FROM users WHERE username = ?", (usernameEntered,))
    lastLogged = cursor.fetchone()[0]
    #updates the last logged in date to the current date
    cursor.execute("UPDATE users SET lastLoggedIn = CURRENT_DATE WHERE username = ?", (usernameEntered, ))
    #saves and closes database
    conn.commit()
    conn.close()
    #sets up the clock
    clock = pygame.time.Clock()
    #sets display
    homeWindow = pygame.display.set_mode((600, 600))
    #establishes functions for the buttons on the screen
    def homePressed():
        pass
    def customisePressed():
        pass
    def leaderboardPressed():
        pass
    def profilePressed():
        pass
    def logOutFunction():
        pass
    def add1():
        pass
    def enter():
        pass
     
     
    #loads home image button  
    homeImage = imageRectButton(homeWindow, pygame.Color(56, 55, 53), (25, 75), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\home.png").convert_alpha(), homePressed)
    #loads customise image button
    customiseImage = imageRectButton(homeWindow, pygame.Color(56, 55, 53), (25, 275), (50, 50),
                                    pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\equalizer.png").convert_alpha(), customisePressed)
    #loads leaderboard image button
    leaderboardImage = imageRectButton(homeWindow, pygame.Color(56, 55, 53), (25, 475), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\podium.png").convert_alpha(), leaderboardPressed)
    #loads account image button
    accountImage = imageRectButton(homeWindow, pygame.Color(56, 55, 53), (537, 12), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\profile.png").convert_alpha(), profilePressed)
    #loads completed checkbox images
    checkedImageA = pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\Ticked Box.png").convert_alpha()
    uncheckedImageA = pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\Empty Box.png").convert_alpha()
    
    #loads the log out button
    logOut = rectButton(homeWindow,
                pygame.Rect(475, 80, 100, 25),
                pygame.Color(46, 94, 59),
                pygame.Color(56, 55, 53),
                "Log Out", 15, logOutFunction)
    #loads the checked and unchecked versions for the completed function
    checkedImage = pygame.transform.scale(checkedImageA, (25, 25))
    uncheckedImage = pygame.transform.scale(uncheckedImageA, (25, 25))



    #instantiates the 'log out' button
    logOut = rectButton(homeWindow,
                        pygame.Rect(475, 80, 100, 25),
                        pygame.Color(46, 94, 59),
                        pygame.Color(56, 55, 53),
                        "Log Out", 15, logOutFunction)
    #instantiates the 'add habit' button
    addButton = rectButton(homeWindow,
                        pygame.Rect(100, 550, 100, 50),
                        pygame.Color(46, 94, 59),
                        pygame.Color(56, 55, 53),
                        "add", 15, add1)
    #instantiates the 'enter Habit' button
    enterHabitButton = rectButton(homeWindow,
                    pygame.Rect(400, 400, 50, 25),
                    pygame.Color(46, 94, 59),
                    pygame.Color(56, 55, 53),
                    "Enter", 15, enter)
    #instantiates the 'edit Habit' button
    editedHabitButton = rectButton(homeWindow,
                    pygame.Rect(400, 400, 50, 25),
                    pygame.Color(46, 94, 59),
                    pygame.Color(56, 55, 53),
                    "Enter", 15, enter)
    #instantiates the 'log Habit Session' button
    loggedTimeButton = rectButton(homeWindow,
                    pygame.Rect(400, 400, 50, 25),
                    pygame.Color(46, 94, 59),
                    pygame.Color(56, 55, 53),
                    "Enter", 15, enter)
    
    
    
    #instantiates the 'habit name' input box for adding habits
    habitNameInput = inputBox(homeWindow, pygame.Rect(150, 250, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    #instantiates the 'daily time' input box for adding habits
    timeDailyInput = inputBox(homeWindow, pygame.Rect(150, 350, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    
    
    #instantiates the 'habit name' input box for editing habits
    editedNameInput = inputBox(homeWindow, pygame.Rect(150, 250, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    #instantiates the 'daily time' input box for editing habits
    editedTimeInput = inputBox(homeWindow, pygame.Rect(150, 350, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    #instantiates the 'log time' input box for logging habit sessions
    loggedTimeInput = inputBox(homeWindow, pygame.Rect(150, 350, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    
    #as a default there should be existing habits related to the account
    existingHabits = True
    
    #connects to the database
    conn = sqlite3.connect('projectDatabase.db')
    cursor = conn.cursor()
    #finds the date now and converts into the format used in sqlite3 for comparison
    date = datetime.datetime.now()
    currentDate = date.strftime("%Y-%m-%d")
    #if the user hasnt logged in today, then reset all their completed stats and streak from resetNewDay() function
    if lastLogged != currentDate:
        resetNewDay(usernameEntered)
        #set last logged in to today
        cursor.execute("UPDATE users SET lastLoggedIn = CURRENT_DATE WHERE username = ?", (usernameEntered,))
        #save database
        conn.commit()
    #fetches all habit IDs and Names related to the user and stores in variable
    cursor.execute("SELECT habitID, habitName FROM habits WHERE username = ?", (usernameEntered,))
    habitsList = cursor.fetchall()
    #fetches all habit IDs and whether they are completed, for all habits related to user and stores in a variable
    cursor.execute("SELECT habitID, completed FROM habits WHERE username = ?", (usernameEntered,))
    completedMap = {row[0]: row[1] for row in cursor.fetchall()}
    #fetches the currency and streak length from the user
    cursor.execute("SELECT currency, streakLength FROM users WHERE username = ?", (usernameEntered,))
    #saves the row, currency and streak as a variable
    userRow = cursor.fetchone()
    currentCurrency = str(userRow[0])
    currentStreak = str(userRow[1])
    #close database
    conn.close()
        
    #sets infinite loop and initialises boolean conditions        
    running = True
    logOutClicked = False
    addingHabit = False
    openMenuHabitID = None
    editingHabit = False
    selectedHabitID = None
    showpopupLog = False
    #sets up pygame rect for the popup when 3 dots are pressed
    popupRect = pygame.Rect(100, 100, 400, 400)
    #sets initial state for habitUI
    habitUI = []
    
    #starts the threading for the failure message (if necessary)
    start = time.monotonic()
    t = threading.Thread(target=runningTime, args=(failure, 3, homeWindow))
    t.start()
    
    while running:
        #fills window
        homeWindow.fill((56, 55, 53))
        
        #draws the images down the side and the add habit button
        homeImage.draw()
        customiseImage.draw()
        leaderboardImage.draw()
        accountImage.draw()
        addButton.draw()
    
        #sets a title for the currency and blits to the screen
        currencyTitleFont = pygame.font.Font('freesansbold.ttf', 15)
        currencyTitleText = currencyTitleFont.render("Currency:", True, (46, 94, 59), (56, 55, 53))
        currencyTitleRect = currencyTitleText.get_rect()
        currencyTitleRect.center = (370, 15)
        homeWindow.blit(currencyTitleText, currencyTitleRect)
        
        #sets the currency as text and blits to the screen
        currencyFont = pygame.font.Font('freesansbold.ttf', 30)
        currencyText = currencyFont.render(currentCurrency, True, (46, 94, 59), (56, 55, 53))
        currencyRect = currencyText.get_rect()
        currencyRect.center = (412, 50)
        homeWindow.blit(currencyText, currencyRect)
        
        #sets the title for the streak and blits it to the screen
        streakTitleFont = pygame.font.Font('freesansbold.ttf', 15)
        streakTitleText = streakTitleFont.render("Streak:", True, (46, 94, 59), (56, 55, 53))
        streakTitleRect = streakTitleText.get_rect()
        streakTitleRect.center = (140, 15)
        homeWindow.blit(streakTitleText, streakTitleRect)
        
        #sets the streak number as text and blits it to the screen
        streakFont = pygame.font.Font('freesansbold.ttf', 30)
        streakText = streakFont.render(currentStreak, True, (46, 94, 59), (56, 55, 53))
        streakRect = streakText.get_rect()
        streakRect.center = (200, 50)
        homeWindow.blit(streakText, streakRect)

        
        
        #sets the title above the list of habits and blits to the screen
        habitsTitleFont = pygame.font.Font('freesansbold.ttf', 25)
        habitsTitleText = habitsTitleFont.render("Habits:", True, (46, 94, 59), (56, 55, 53))
        habitsTitleRect = habitsTitleText.get_rect()
        habitsTitleRect.center = (175, 100)
        homeWindow.blit(habitsTitleText, habitsTitleRect)

        #if there are no existing habits...
        if not existingHabits:
            #display that there are no habits and blit to screen
            emptyFont = pygame.font.Font('freesansbold.ttf', 17)
            emptyText = emptyFont.render("No Existing Habits", True, (46, 94, 59), (56, 55, 53))
            emptyRect = emptyText.get_rect()
            emptyRect.center = (225, 200)
            homeWindow.blit(emptyText, emptyRect)
            
        #if there are existing habits           
        else:
            #sets font and initial variables: starting position and line spacing
            habitFont = pygame.font.Font('freesansbold.ttf', 18)
            startY = 150
            lineSpacing = 40
            habitUI.clear()
            #for each habit in the habits lis
            for index, habit in enumerate(habitsList):
                #sets current habit ID to the first position in habit array
                habitID = habit[0]
                #sets current hait name to the second position in habit array
                habitName = habit[1]
                #finds what row it should be using the index and variables initialised earlier
                rowY = startY + index * lineSpacing
                #makes a rect in that position
                rowRect = pygame.Rect(110, rowY - 5, 380, 30)
                #draws that rect to the screen
                pygame.draw.rect(homeWindow, (46, 94, 59), rowRect, 2)
                #sets text to the name of the current habit
                text = f"{habitName}"
                #renders the habit name text
                habitSurface = habitFont.render(text, True, (46, 94, 59))
                #blits the screen with the habit text
                homeWindow.blit(habitSurface, (120, rowY))
                #sets rect for the dots, log time and checkbox, for each habit
                dotsRect = pygame.Rect(460, rowY, 25, 20)
                logTimeRect = pygame.Rect(435, rowY, 25, 20)
                checkboxRect = pygame.Rect(395, rowY-3, 25, 20)
                #draws the dots, log time option and checkbox
                pygame.draw.rect(homeWindow, (56, 55, 53), dotsRect, 2)
                pygame.draw.rect(homeWindow, (56, 55, 53), logTimeRect, 2)
                pygame.draw.rect(homeWindow, (56, 55, 53), checkboxRect, 2)
                #sets the dots and logTime font and surface
                dotFont = pygame.font.Font(None, 25)
                dotsSurface = dotFont.render("...", True, (46, 94, 59))
                logTimeSurface = dotFont.render("+", True, (46, 94, 59))
                completed = completedMap.get(habitID, 0)
                #if they have completed the given habit...
                if completed:
                    #blit the checked version of checkbox
                    homeWindow.blit(checkedImage, checkboxRect)
                #if they have not completed the given habit...
                else:
                    #blit the unchecked version of the checkbox
                    homeWindow.blit(uncheckedImage, checkboxRect)
                #blit the dots and + at the row position
                homeWindow.blit(dotsSurface, (465, rowY - 3))
                homeWindow.blit(logTimeSurface, (435, rowY))
                #adds habitID, dotsRect, rowY and logTimeRect to the habitUI array
                habitUI.append({
                    "habitID": habitID,
                    "dotsRect": dotsRect,
                    "rowY": rowY,
                    "logTimeRect": logTimeRect
                })
                
                
        #for each value in habitUI      
        for item in habitUI:
            #if the 3 dots are clicked, meaning menu opens for given habit...
            if openMenuHabitID == item["habitID"]:
                #set the menu rect and draw the menu rectangle
                menuRect = pygame.Rect(430, item["rowY"] + 25, 120, 60)
                pygame.draw.rect(homeWindow, (46, 94, 59), menuRect)
                
                #sets the pygame rect for the options to edit or delete the habit, in the 3 dots
                item["editRect"] = pygame.Rect(430, item["rowY"] + 25, 120, 30)
                item["deleteRect"] = pygame.Rect(430, item["rowY"] + 55, 120, 30)
                
                #draws the rect for editing and deleting habit
                pygame.draw.rect(homeWindow, (46, 94, 59), item["editRect"])
                pygame.draw.rect(homeWindow, (46, 94, 59), item["deleteRect"])
                
                #sets font
                font = pygame.font.Font(None, 20)
                
                #blits the edit and delete option at row Y
                homeWindow.blit(font.render("Edit", True, (56, 55, 53)),
                        (440, item["rowY"] + 32))
                homeWindow.blit(font.render("Delete", True, (56, 55, 53)),
                        (440, item["rowY"] + 62))



        #if the add habit button has been pressed...
        if addingHabit:
            #shade screen
            overlay = pygame.Surface(homeWindow.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 80))
            #blits the shaded version
            homeWindow.blit(overlay, (0, 0))
            #draw rectangles on top
            pygame.draw.rect(homeWindow, (56, 55, 53), popupRect)
            pygame.draw.rect(homeWindow, (46, 94, 59), popupRect, 2)
            #draw input boxes
            habitNameInput.draw()
            timeDailyInput.draw()
            enterHabitButton.draw()
            
            #gives name input box a title and blits to the screen
            enterNameFont = pygame.font.Font('freesansbold.ttf', 17)
            enterNameText = enterNameFont.render("Habit Name", True, (46, 94, 59), (56, 55, 53))
            enterNameRect = enterNameText.get_rect()
            enterNameRect.center = (200, 220)
            homeWindow.blit(enterNameText, enterNameRect)
            #gives time input box a title and blits to the screen
            timeFont = pygame.font.Font('freesansbold.ttf', 17)
            timeText = timeFont.render("Time spent Daily (minutes)", True, (46, 94, 59), (56, 55, 53))
            timeRect = timeText.get_rect()
            timeRect.center = (260, 320)
            homeWindow.blit(timeText, timeRect)
            #gives the adding window a title and blits to the screen
            addingTitleFont = pygame.font.Font('freesansbold.ttf', 25)
            addingTitleText = addingTitleFont.render("Add a New Habit:", True, (46, 94, 59), (56, 55, 53))
            addingTitleRect = addingTitleText.get_rect()
            addingTitleRect.center = (250, 175)
            homeWindow.blit(addingTitleText, addingTitleRect)
        
        
        
        #if a Habit is being edited
        elif editingHabit:
            #shade screen
            overlay = pygame.Surface(homeWindow.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 80))
            #blit the shaded overlay
            homeWindow.blit(overlay, (0, 0))
            #draw rectanges on top
            pygame.draw.rect(homeWindow, (56, 55, 53), popupRect)
            pygame.draw.rect(homeWindow, (46, 94, 59), popupRect, 2)
            #draw input boxes
            editedNameInput.draw()
            editedTimeInput.draw()
            editedHabitButton.draw()
            
            #gives the edited name input box a title and blits to the screen
            enterEditNameFont = pygame.font.Font('freesansbold.ttf', 17)
            enterEditNameText = enterEditNameFont.render("Edited Habit Name", True, (46, 94, 59), (56, 55, 53))
            enterEditNameRect = enterEditNameText.get_rect()
            enterEditNameRect.center = (200, 220)
            homeWindow.blit(enterEditNameText, enterEditNameRect)
            #gives the edited time input box a title and blits to the screen
            timeEditFont = pygame.font.Font('freesansbold.ttf', 17)
            timeEditText = timeEditFont.render("Edited Time spent Daily (minutes)", True, (46, 94, 59), (56, 55, 53))
            timeEditRect = timeEditText.get_rect()
            timeEditRect.center = (260, 320)
            homeWindow.blit(timeEditText, timeEditRect)
            #gives the editing window a title and blits to the screen
            editTitleFont = pygame.font.Font('freesansbold.ttf', 25)
            editTitleText = editTitleFont.render("Edit Habit:", True, (46, 94, 59), (56, 55, 53))
            editTitleRect = editTitleText.get_rect()
            editTitleRect.center = (250, 175)
            homeWindow.blit(editTitleText, editTitleRect)
        
        #if the popup for logging habit is true (they pressed the +)
        elif showpopupLog:
            #shades screen
            overlay = pygame.Surface(homeWindow.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 80))
            #blit the shaded overlay
            homeWindow.blit(overlay, (0, 0))
            #draw rectanges on top
            pygame.draw.rect(homeWindow, (56, 55, 53), popupRect)
            pygame.draw.rect(homeWindow, (46, 94, 59), popupRect, 2)
            #draw input boxes
            loggedTimeInput.draw()
            loggedTimeButton.draw()
        
            #gives the logged time input box a title and blits to the screen
            loggedTimeFont = pygame.font.Font('freesansbold.ttf', 17)
            loggedTimeText = loggedTimeFont.render("Time spent on Habit", True, (46, 94, 59), (56, 55, 53))
            loggedTimeRect = loggedTimeText.get_rect()
            loggedTimeRect.center = (260, 320)
            homeWindow.blit(loggedTimeText, loggedTimeRect)
            #gives the logging time window a title and blits to the screen
            logTitleFont = pygame.font.Font('freesansbold.ttf', 25)
            logTitleText = logTitleFont.render("Log Habit Session:", True, (46, 94, 59), (56, 55, 53))
            logTitleRect = logTitleText.get_rect()
            logTitleRect.center = (250, 175)
            homeWindow.blit(logTitleText, logTitleRect)

        #if the user has pressed the user icon, show the log out button option
        if logOutClicked == True:
            logOut.draw()
        
        #draws the rectangles that split the window into parts
        pygame.draw.rect(homeWindow, (50, 94, 63), (0, 0, 100, 600), 2)
        pygame.draw.rect(homeWindow, (50, 94, 63), (525, 0, 75, 75), 2)
        pygame.draw.rect(homeWindow, (50, 94, 63), (100, 0, 212, 75), 2)
        pygame.draw.rect(homeWindow, (50, 94, 63), (312, 0, 213, 75), 2)
    
    
        #any events in pygame            
        for event in pygame.event.get():
            #if user presses to exit then shut the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #if the user presses with their mouse...
            if event.type == pygame.MOUSEBUTTONDOWN:
                #and if their also adding a new habit...
                if addingHabit:
                    #and if they click the habit name input box...
                    if habitNameInput.rect.collidepoint(event.pos):
                        #activate the name box and deactivate the time box
                        habitNameInput.activate()
                        timeDailyInput.deactivate()
                        
                    #if they click the habit time input box...
                    elif timeDailyInput.rect.collidepoint(event.pos):
                        #activate the time box and deactivate the name box
                        timeDailyInput.activate()
                        habitNameInput.deactivate()
                        
                    #if the user presses to enter this new habit
                    elif enterHabitButton.rect.collidepoint(event.pos):
                        #call the add habit function and store its returning values as username and failure reason
                        addedUsername, addFailure = addHabit(habitNameInput.userText, timeDailyInput.userText, usernameEntered)
                        #return these to the main program
                        return "refreshHome", addedUsername, addFailure
                    #if they press on the popup but not the input box...
                    elif popupRect.collidepoint(event.pos):
                        #deactivate both input boxes
                        habitNameInput.deactivate()
                        timeDailyInput.deactivate()                    
                    #if they pressed outside of the window...
                    elif not popupRect.collidepoint(event.pos):
                        #turn off the adding habit, removing the window
                        addingHabit = False
                
                #if they are editing an existing habit...
                elif editingHabit:
                    #and if they click the edit name input box
                    if editedNameInput.rect.collidepoint(event.pos):
                        #activate the edit name box and deactivate the edited time box
                        editedNameInput.activate()
                        editedTimeInput.deactivate()
                        
                    #if they click the edit time input box
                    elif editedTimeInput.rect.collidepoint(event.pos):
                        #activate the edit time box and deactivate the edited name box
                        editedTimeInput.activate()
                        editedNameInput.deactivate()
                    
                    #if they press to enter the new version of the habit
                    elif editedHabitButton.rect.collidepoint(event.pos):
                        #call the edit habit function and store returning values as username and failure reason
                        editUser, editFailed = editHabit(selectedHabitID, editedTimeInput.userText, editedNameInput.userText, usernameEntered)
                        #resets the values for userText for both input boxes
                        editedNameInput.userText = ""
                        editedTimeInput.userText = ""
                        #sets editing habit to false as its been entered
                        editingHabit = False
                        #returns the other values to main program
                        return "refreshHome", editUser, editFailed
                    #if they press anywhere outside of the input box...
                    elif popupRect.collidepoint(event.pos):
                        #set both input boxes to false
                        editedTimeInput.deactivate()
                        editedNameInput.deactivate()
                    #if they press outside the popup window...
                    elif not popupRect.collidepoint(event.pos):
                        #deactivate both and set editing habit to false
                        editedTimeInput.deactivate()
                        editedNameInput.deactivate()
                        editingHabit = False
                
                #if pop up window is showing for the log habit session...
                elif showpopupLog:
                    #if they click the log time box...
                    if loggedTimeInput.rect.collidepoint(event.pos):
                        #activate the log time box
                        loggedTimeInput.activate()
                    #if they click the enter button
                    elif loggedTimeButton.rect.collidepoint(event.pos):
                        #call log habit function and store returning values as username and failure reason
                        logUser, logFail = logHabit(selectedHabitID, loggedTimeInput.userText, usernameEntered)
                        #sets value to empty once completed
                        loggedTimeInput.userText = ""
                        #removes the pop up window
                        showpopupLog = False
                        #returns the other values to the main program
                        return "refreshHome", logUser, logFail
                    #if while logging they press outside the popup then shut the pop up and set to false
                    elif not popupRect.collidepoint(event.pos):
                        loggedTimeInput.deactivate()
                        showpopupLog = False

                #if there are no popups present
                else:
                    #checking each habit...
                    for item in habitUI:
                        #if user presses the log time (+) option...
                        if item["logTimeRect"].collidepoint(event.pos):
                            #set selected habit to the correct ID and the popup to true to display it
                            selectedHabitID = item["habitID"]
                            showpopupLog = True
                            
                        #if user presses the menu (...) option...
                        if item["dotsRect"].collidepoint(event.pos):
                            #set selected menu to that habit ID if it doesnt already
                            openMenuHabitID = item["habitID"] if openMenuHabitID != item["habitID"] else None
                            
                        #if the popup menu is open...
                        if openMenuHabitID == item["habitID"]:
                            #and if they choose to edit...
                            if "editRect" in item and item["editRect"].collidepoint(event.pos):
                                #set editing to true
                                editingHabit = True
                                selectedHabitID = item["habitID"]
                            #if they choose to delete...
                            elif "deleteRect" in item and item["deleteRect"].collidepoint(event.pos):
                                #call the delete function and store returning values as username and failure reason
                                deleteUsername, deleteFailure = deleteHabit(item["habitID"], usernameEntered)
                                #returns these values to the main program
                                return "refreshHome", deleteUsername, deleteFailure

                    #if they have pressed add habit then set it to true
                    if addButton.rect.collidepoint(event.pos):
                        addingHabit = True
                    #if they press the account in the corner then toggle the log out menu popping up
                    elif accountImage.imageRect.collidepoint(event.pos):
                        logOutClicked = not logOutClicked
                    #if they press log out then return to the start page
                    elif logOut.rect.collidepoint(event.pos) and logOutClicked:
                        return "start"
                    #if click the home page then take user to home page
                if homeImage.imageRect.collidepoint(event.pos):
                    homePress = "main Page"
                    return homePress
                elif accountImage.imageRect.collidepoint(event.pos):
                    logOutClicked = not logOutClicked
                #if clicked on customise page then take user there
                elif customiseImage.imageRect.collidepoint(event.pos):
                    customisePress = "customise Page"
                    return customisePress
                #if clicked on leaderboard page then take user there
                elif leaderboardImage.imageRect.collidepoint(event.pos):
                    leaderboardPress = "leaderboard Page"
                    return leaderboardPress
                #if user presses account image, they may want to log out so show the log in button (above)
                elif accountImage.imageRect.collidepoint(event.pos):
                    logOutClicked = True
                #if user logs out take them to the start page
                elif logOut.rect.collidepoint(event.pos):
                    return "start"
                else:
                    logOutClicked = False
            #if they press a key...
            if event.type == pygame.KEYDOWN:
                #checking every single input box
                for box in [habitNameInput, timeDailyInput, editedNameInput, editedTimeInput, loggedTimeInput]:
                    #if any are active...
                    if box.active:
                        #and if they press backspace then delete the last character
                        if event.key == pygame.K_BACKSPACE:
                            box.delete()
                        #if they type anything else then add it to the user text using OOP methods
                        else:
                            box.typing(event.unicode)

        #handles all failure messages...
        #if there was an issue with adding the habit then give a failure message
        if failed == "addAlertError":
            if t.is_alive():
                    failure(homeWindow, f"please check your entered time \n and try again, (must be > 0) {round(time.monotonic() - start, 1)}")                 
        #if added successfully then give a message
        elif failed == "addAlertWorked":
            if t.is_alive():
                    failure(homeWindow, f"Habit Added Successfully {round(time.monotonic() - start, 1)}")
        
        #if successfully deleted then give message
        elif failed == "deleteSuccess":
            if t.is_alive():
                failure(homeWindow, f"Habit Removed Successfully {round(time.monotonic() - start, 1)}")
        
        #if edited successfully then give a failure message
        elif failed == "editSuccess":
            if t.is_alive():
                    failure(homeWindow, f"Habit Edited Successfully {round(time.monotonic() - start, 1)}")
        #if theres an issue with editing the message the give failure message
        elif failed == "editFail":
            if t.is_alive():
                    failure(homeWindow, f"An error occured when editing, \n please try again {round(time.monotonic() - start, 1)}")
        
        #if logged successfully then give a mesasage
        elif failed == "logSuccess":
            if t.is_alive():
                    failure(homeWindow, f"Session Logged Successfully {round(time.monotonic() - start, 1)}")
        #if theres an issue with logging then give failure message
        elif failed == "logFail":
            if t.is_alive():
                    failure(homeWindow, f"An error occured when logging \n this session, please try again {round(time.monotonic() - start, 1)}")
        #flip display
        pygame.display.flip()
        clock.tick(60)