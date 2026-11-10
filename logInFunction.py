#import relevant libraries and called functions
import sys
import pygame
import sqlite3
import rectangleButtonClass
import time
import threading
from checkUserData import checkLogIn
from failureMessage import failure
from failureMessage import runningTime
pygame.init()
def logIn(failed):
    #initialises fonts, clocks and windows
    clock = pygame.time.Clock()
    logInWindow = pygame.display.set_mode((600, 600))
    logInFont = pygame.font.Font(None, 32)
    #instantiates the username input box from the inputBox class
    usernameInput = rectangleButtonClass.inputBox(logInWindow, pygame.Rect(150, 150, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    #instantiates the password input box from the inputBox class
    passwordInput = rectangleButtonClass.inputBox(logInWindow, pygame.Rect(150, 250, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    #Initialises subfunction for the function of the back button
    def goBack():
        returningBack = True
    #Initialises the subfunction for the function of the enter button
    def check():
        checking = True
    #instantiates the back button from the rectButton class
    backButton = rectangleButtonClass.rectButton(logInWindow,
                                                pygame.Rect(25, 75, 50, 25),
                                                pygame.Color(46, 94, 59),
                                                pygame.Color(56, 55, 53),
                                                "back", 15, goBack)
    #instantiates the enter button from the rectButton class
    enterButton = rectangleButtonClass.rectButton(logInWindow,
                                                pygame.Rect(500, 250, 50, 25),
                                                pygame.Color(46, 94, 59),
                                                pygame.Color(56, 55, 53),
                                                "enter", 15, check)
    
    #starts the failure message from failed attempts at logging in
    start = time.monotonic()
    t = threading.Thread(target=runningTime, args=(failure, 3, logInWindow))
    t.start()
    #sets initialised variables
    logInPage = True
    #infinite loop until stopped
    while logInPage:
            
        #for any pygame event...
        for event in pygame.event.get():
            #if we quit then stop returning anything
            if event.type == pygame.QUIT:
                return None
            #if we click then...
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if it is clicked inside the username Input box then activate it and deactivate all others
                if usernameInput.rect.collidepoint(event.pos):
                    usernameInput.activate()
                    passwordInput.deactivate()
                #if it is clicked inside the password Input box then activate it and deactivate all others
                elif passwordInput.rect.collidepoint(event.pos):
                    usernameInput.deactivate()
                    passwordInput.activate()
                #if the back button is pressed then return "start" which in the main program takes back to start page
                elif backButton.rect.collidepoint(event.pos):
                    return "start"
                #if the enter button is pressed then check the details exist via calling an external function
                elif enterButton.rect.collidepoint(event.pos):
                    resultChecking = checkLogIn(usernameInput.userText, passwordInput.userText)
                    #username and password entered texts need to stop updating at this point
                    passwordActive = False
                    usernameActive = False
                    #returns this so the main program can respond accordingly
                    return resultChecking
                #if clicked anywhere else then decactivate both input boxes
                else:
                    usernameInput.deactivate()
                    passwordInput.deactivate()
            #if a key is pressed...        
            if event.type == pygame.KEYDOWN:
                #and if the username box is active...
                if usernameInput.active:
                    #and if we press backspace then delete the last character
                    if event.key == pygame.K_BACKSPACE:
                        usernameInput.delete()
                    #also if we press anything else then add it to the username entered text
                    else:
                        usernameInput.typing(event.unicode)
                #also if the password box is active
                if passwordInput.active:
                    #and if we press backspace delete the last character
                    if event.key == pygame.K_BACKSPACE:
                        passwordInput.delete()
                    #if anything else is pressed then add it to the password entered text
                    else:
                        passwordInput.typing(event.unicode)
        #fills window, and draws all buttons/boxes
        logInWindow.fill((56, 55, 53))    
        enterButton.draw()
        backButton.draw()
        usernameInput.draw()
        passwordInput.draw()
        #creates the font, renders and blits text at given coordinates for the Title of the page
        logInTitleFont = pygame.font.Font('freesansbold.ttf', 30)
        logInTitleText = logInTitleFont.render("Log In", True, (46, 94, 59), (56, 55, 53))
        logInTitleRect = logInTitleText.get_rect()
        logInTitleRect.center = (60, 50)
        logInWindow.blit(logInTitleText, logInTitleRect)
        
        #creates the font, renders and blits text at given coordinates for the username text
        usernameFont = pygame.font.Font('freesansbold.ttf', 15)
        usernameText = usernameFont.render("Username:", True, (46, 94, 59), (56, 55, 53))
        usernameRect = usernameText.get_rect()
        usernameRect.center = (100, 160)
        logInWindow.blit(usernameText, usernameRect)
        
        #creates the font, renders and blits text at given coordinates for the password text
        passwordFont = pygame.font.Font('freesansbold.ttf', 15)
        passwordText = passwordFont.render("Password:", True, (46, 94, 59), (56, 55, 53))
        passwordRect = passwordText.get_rect()
        passwordRect.center = (100, 260)
        logInWindow.blit(passwordText, passwordRect)        
        
        #if the log in attempt was unsuccessful...
        if failed:
            if t.is_alive():
                #run the failure message with the below message
                failure(logInWindow, f"username or password is not recognised, \n please try again {round(time.monotonic() - start, 1)}")            
            
        #refresh the display    
        pygame.display.flip()