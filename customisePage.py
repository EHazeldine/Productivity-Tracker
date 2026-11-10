#imports any libraries and functions made
import pygame
pygame.init()
import sqlite3
import sys
from rectangleButtonClass import imageRectButton
from rectangleButtonClass import rectButton
def customisePage(usernameEntered):
    #initialises the pygame window
    customiseWindow = pygame.display.set_mode((600, 600))
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
        currentCurrency = str(cursor.fetchone()[0])
        currentCurrencyLength = len(currentCurrency)
        #sets the font, text, rect and center for the currency window
        currencyFont = pygame.font.Font('freesansbold.ttf', 30)
        currencyText = currencyFont.render(currentCurrency, True, (46, 94, 59), (56, 55, 53))
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
        #sets the length, font, text, rect and center for the streak window
        currentStreakLength = len(currentStreak)
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
        
        
    #loads home image button  
    homeImage = imageRectButton(customiseWindow, pygame.Color(56, 55, 53), (25, 75), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\home.png").convert_alpha(), homePressed)
    #loads customise image button
    customiseImage = imageRectButton(customiseWindow, pygame.Color(56, 55, 53), (25, 275), (50, 50),
                                    pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\equalizer.png").convert_alpha(), customisePressed)
    #loads leaderboard image button
    leaderboardImage = imageRectButton(customiseWindow, pygame.Color(56, 55, 53), (25, 475), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\podium.png").convert_alpha(), leaderboardPressed)
    #loads account image button
    accountImage = imageRectButton(customiseWindow, pygame.Color(56, 55, 53), (537, 12), (50, 50),
                                pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\profile.png").convert_alpha(), profilePressed)
    #loads completed checkbox images
    checkedImageA = pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\Ticked Box.png").convert_alpha()
    uncheckedImageA = pygame.image.load("C:\\Users\\eddie\\OneDrive - Embrace MAT\\Computer Science\\NEA Project\\Icons I might use\\Empty Box.png").convert_alpha()
    
    #loads the log out button
    logOut = rectButton(customiseWindow,
                pygame.Rect(475, 80, 100, 25),
                pygame.Color(46, 94, 59),
                pygame.Color(56, 55, 53),
                "Log Out", 15, logOutFunction)
    #sets infinite running loop
    running = True
    logOutClicked = False
    while running:
        #fills the window with a background
        customiseWindow.fill((56, 55, 53))
        #draws the buttons down the left hand side
        homeImage.draw()
        customiseImage.draw()
        leaderboardImage.draw()
        accountImage.draw()
        #draws rectangles to break up the window into sections
        pygame.draw.rect(customiseWindow, (50, 94, 63), (0, 0, 100, 600), 2)
        pygame.draw.rect(customiseWindow, (50, 94, 63), (525, 0, 75, 75), 2)
        pygame.draw.rect(customiseWindow, (50, 94, 63), (100, 0, 212, 75), 2)
        pygame.draw.rect(customiseWindow, (50, 94, 63), (312, 0, 213, 75), 2)
        #loads currency and streak, displays on window
        displayCurrency(usernameEntered, customiseWindow)
        displayStreak(usernameEntered, customiseWindow)
        #adds a title
        customiseTitleFont = pygame.font.Font('freesansbold.ttf', 30)
        customiseTitleText = customiseTitleFont.render("Coming Soon :)", True, (46, 94, 59), (56, 55, 53))
        customiseTitleRect = customiseTitleText.get_rect()
        customiseTitleRect.center = (300, 300)
        customiseWindow.blit(customiseTitleText, customiseTitleRect)
        
        #if the account image is pressed then give the option to log out
        if logOutClicked == True:
            logOut.draw()
            #refresh display
        pygame.display.flip()
        #for any events
        for event in pygame.event.get():
            #if the screen is clicked...   
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if clicked the home page then take user to home page
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
                #remove the log out option from the screen
                else:
                    logOutClicked = False   