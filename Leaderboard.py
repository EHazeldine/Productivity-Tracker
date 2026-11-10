#imports any libraries and functions made
import pygame
pygame.init()
import sqlite3
import sys
from rectangleButtonClass import imageRectButton
from rectangleButtonClass import rectButton
def leaderboard(usernameEntered):
    #intialises the window
    leaderboardWindow = pygame.display.set_mode((600, 600))
    #establishes functions for the buttons on the screen, in this case they are all empty
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
    #displays the currency that the current logged in user has
    def displayCurrency(enteredUsername, window):
        #connects to the database and fetches the currency for the logged in user
        conn = sqlite3.connect("projectDatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT currency FROM users WHERE username = ?",
                   (usernameEntered, ))
        #saves the currency to variable
        currentCurrencyA = str(cursor.fetchone()[0])
        #sets the font, text, rect and center for the currency window
        currencyFont = pygame.font.Font('freesansbold.ttf', 30)
        currencyText = currencyFont.render(currentCurrencyA, True, (46, 94, 59), (56, 55, 53))
        currencyRect = currencyText.get_rect()
        currencyRect.center = (412, 50)
        #blits the text onto the window
        window.blit(currencyText, currencyRect)

        #sets a title for the currency and blits to the screen
        currencyTitleFont = pygame.font.Font('freesansbold.ttf', 15)
        currencyTitleText = currencyTitleFont.render("Currency:", True, (46, 94, 59), (56, 55, 53))
        currencyTitleRect = currencyTitleText.get_rect()
        currencyTitleRect.center = (370, 15)
        window.blit(currencyTitleText, currencyTitleRect)

    def displayStreak(enteredUsername, window):
        #connects to the database
        conn = sqlite3.connect("projectDatabase.db")
        cursor = conn.cursor()
        #queries the length of the streak the user currently has 
        cursor.execute("SELECT streakLength FROM users WHERE username = ?",
                   (usernameEntered, ))
        #saves this in variable
        currentStreak = str(cursor.fetchone()[0])
        currentStreakLength = len(currentStreak)
        #sets the length, font, text, rect and center for the streak window
        streakFont = pygame.font.Font('freesansbold.ttf', 30)
        streakText = streakFont.render(currentStreak, True, (46, 94, 59), (56, 55, 53))
        streakRect = streakText.get_rect()
        streakRect.center = (200, 50)
        #blits the text onto the window
        window.blit(streakText, streakRect)
        
        #sets the title for the streak and blits it to the screen
        streakTitleFont = pygame.font.Font('freesansbold.ttf', 15)
        streakTitleText = streakTitleFont.render("Streak:", True, (46, 94, 59), (56, 55, 53))
        streakTitleRect = streakTitleText.get_rect()
        streakTitleRect.center = (140, 15)
        window.blit(streakTitleText, streakTitleRect)
        
    def leaderboardLoad():
        #connects to the database
        conn = sqlite3.connect("projectDatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username, currency FROM users ORDER BY currency DESC LIMIT 10")
        #takes a descending list of the 10 users with highest currency
        usersList = cursor.fetchall()
        #takes the start Y value and line spacing
        startY = 150
        lineSpacing = 40
        #sets fonts
        habitFont = pygame.font.Font('freesansbold.ttf', 18)
        #for each user, on their own line...
        for index, habit in enumerate(usersList):
            #unpacks for the user at index
            usersInfo = usersList[index]
            #takes username
            nameofusers = usersInfo[0]
            #takes currency of the user
            currencyofusers = usersInfo[1]
            #finds what position on screen the user should be in
            rowY = startY + index * lineSpacing
            #makes a rect for the coordinates
            rowRect = pygame.Rect(110, rowY - 5, 380, 30)
            #draws the rect
            pygame.draw.rect(leaderboardWindow, (46, 94, 59), rowRect, 2)
            #takes the name as text
            nameText = f"{nameofusers}"
            #blits this name onto the screen
            habitSurface = habitFont.render(nameText, True, (46, 94, 59))
            leaderboardWindow.blit(habitSurface, (120, rowY))
            #takes currency as text and blits onto screen
            currencyText = f"{currencyofusers}"
            habitSurface = habitFont.render(currencyText, True, (46, 94, 59))
            leaderboardWindow.blit(habitSurface, (420, rowY))
            #save + close db
            conn.commit()
        conn.close()
    #loads home image button  
    homeImage = imageRectButton(leaderboardWindow, pygame.Color(56, 55, 53), (25, 75), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\home.png").convert_alpha(), homePressed)
    #loads customise image button
    customiseImage = imageRectButton(leaderboardWindow, pygame.Color(56, 55, 53), (25, 275), (50, 50),
                                    pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\equalizer.png").convert_alpha(), customisePressed)
    #loads leaderboard image button
    leaderboardImage = imageRectButton(leaderboardWindow, pygame.Color(56, 55, 53), (25, 475), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\podium.png").convert_alpha(), leaderboardPressed)
    #loads account image button
    accountImage = imageRectButton(leaderboardWindow, pygame.Color(56, 55, 53), (537, 12), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\profile.png").convert_alpha(), profilePressed)
    
    #loads the log out button
    logOut = rectButton(leaderboardWindow,
                pygame.Rect(475, 80, 100, 25),
                pygame.Color(46, 94, 59),
                pygame.Color(56, 55, 53),
                "Log Out", 15, logOutFunction)
    #sets infinite loop and sets initial variables
    running = True
    logOutClicked = False
    while running:
        #fills the window baackground
        leaderboardWindow.fill((56, 55, 53))
        #draws the image buttons down the left side of screen
        homeImage.draw()
        customiseImage.draw()
        leaderboardImage.draw()
        accountImage.draw()
        #loads the leaderabord on the screen
        leaderboardLoad()
        #sets the leaderboard title, font texxt, rect and center
        leaderboardTitleFont = pygame.font.Font('freesansbold.ttf', 25)
        leaderboardTitleText = leaderboardTitleFont.render("leaderboard:", True, (46, 94, 59), (56, 55, 53))
        leaderboardTitleRect = leaderboardTitleText.get_rect()
        leaderboardTitleRect.center = (200, 100)
        #blits on the screen
        leaderboardWindow.blit(leaderboardTitleText, leaderboardTitleRect)
        #draws rectangles taht split up the window into parts
        pygame.draw.rect(leaderboardWindow, (50, 94, 63), (0, 0, 100, 600), 2)
        pygame.draw.rect(leaderboardWindow, (50, 94, 63), (525, 0, 75, 75), 2)
        pygame.draw.rect(leaderboardWindow, (50, 94, 63), (100, 0, 212, 75), 2)
        pygame.draw.rect(leaderboardWindow, (50, 94, 63), (312, 0, 213, 75), 2)
        #displays the streak and currency
        displayCurrency(usernameEntered, leaderboardWindow)
        displayStreak(usernameEntered, leaderboardWindow)
        #if user presses the account button then enable the option to log out
        if logOutClicked == True:
            logOut.draw()
        #refresh the display
        pygame.display.flip()
        for event in pygame.event.get():
            #for any other events on the screen when not adding a habit or other actions        
            if event.type == pygame.MOUSEBUTTONDOWN:
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