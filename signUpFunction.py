#import relevant libraries and called functions
import sys
import pygame
import sqlite3
import rectangleButtonClass
import time
import threading
from checkUserData import checkSignUp
from failureMessage import failure
from failureMessage import runningTime
pygame.init()
def signUp(failed):
    #initialises font, the window and the clock
    clock = pygame.time.Clock()
    signUpWindow = pygame.display.set_mode((600, 600))
    signUpFont = pygame.font.Font(None, 32)
    #instantiates the username input box from the inputBox class
    newUsernameInput = rectangleButtonClass.inputBox(signUpWindow, pygame.Rect(150, 150, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    #instantiates the password input box from the inputBox class
    newPasswordInput = rectangleButtonClass.inputBox(signUpWindow, pygame.Rect(150, 250, 300, 25),
                                                pygame.Color(50, 94, 63), pygame.Color(90, 190, 220),
                                                None, (255, 255, 255), 15, "", False, "")
    #Initialises subfunction for the function of the back button
    def goBack():
        returningBack = True
    #Initialises the subfunction for the function of the enter button
    def check():
        checking = True
    #instantiates the back button from the rectButton class
    backButton = rectangleButtonClass.rectButton(signUpWindow,
                                                pygame.Rect(25, 75, 50, 25),
                                                pygame.Color(46, 94, 59),
                                                pygame.Color(56, 55, 53),
                                                "back", 15, goBack)
    #instantiates the enter button from the rectButton class
    enterButton = rectangleButtonClass.rectButton(signUpWindow,
                                                pygame.Rect(500, 250, 50, 25),
                                                pygame.Color(46, 94, 59),
                                                pygame.Color(56, 55, 53),
                                                "enter", 15, check)
    #sets up time for threading, if a failure message is needed
    start = time.monotonic()
    t = threading.Thread(target=runningTime, args=(failure, 3, signUpWindow))
    t.start()    
    #starts the infinite signUpPage loop
    signUpPage = True
    while signUpPage:
        #for any pygame event...
        for event in pygame.event.get():
            #if we quit then stop returning anything
            if event.type == pygame.QUIT:
                return None
            #if we click then...
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if it is clicked inside the username Input box then activate it and deactivate all others
                if newUsernameInput.rect.collidepoint(event.pos):
                    newUsernameInput.activate()
                    newPasswordInput.deactivate()
                #if it is clicked inside the password Input box then activate it and deactivate all others
                elif newPasswordInput.rect.collidepoint(event.pos):
                    newUsernameInput.deactivate()
                    newPasswordInput.activate()
                #if the back button is pressed then return "start" which in the main program takes back to start page
                elif backButton.rect.collidepoint(event.pos):
                    return "start"
                #if the enter button is pressed then check the details exist via calling an external function
                elif enterButton.rect.collidepoint(event.pos):
                    resultChecking = checkSignUp(newUsernameInput.userText, newPasswordInput.userText)
                    #username and password entered texts need to stop updating at this point
                    passwordActive = False
                    usernameActive = False
                    #returns this so the main program can respond accordingly
                    return resultChecking
                #if clicked anywhere else then decactivate both input boxes
                else:
                    newUsernameInput.deactivate()
                    newPasswordInput.deactivate()
            #if a key is pressed...        
            if event.type == pygame.KEYDOWN:
                #and if the username box is active...
                if newUsernameInput.active:
                    #and if we press backspace then delete the last character
                    if event.key == pygame.K_BACKSPACE:
                        newUsernameInput.delete()
                    #also if we press anything else then add it to the username entered text
                    else:
                        newUsernameInput.typing(event.unicode)
                #also if the password box is active
                if newPasswordInput.active:
                    #and if we press backspace delete the last character
                    if event.key == pygame.K_BACKSPACE:
                        newPasswordInput.delete()
                    #if anything else is pressed then add it to the password entered text
                    else:
                        newPasswordInput.typing(event.unicode)
        #fills window, and draws all buttons/boxes
        signUpWindow.fill((56, 55, 53))    
        enterButton.draw()
        backButton.draw()
        newUsernameInput.draw()
        newPasswordInput.draw()
        
        #renders the title for the sign up page
        signUpTitleFont = pygame.font.Font('freesansbold.ttf', 30)
        signUpTitleText = signUpTitleFont.render("Sign Up", True, (46, 94, 59), (56, 55, 53))
        signUpTitleRect = signUpTitleText.get_rect()
        signUpTitleRect.center = (75, 50)
        #blits to the screen
        signUpWindow.blit(signUpTitleText, signUpTitleRect)
        
        #renders the username title for the sign up page
        usernameFont = pygame.font.Font('freesansbold.ttf', 15)
        usernameText = usernameFont.render("Username:", True, (46, 94, 59), (56, 55, 53))
        usernameRect = usernameText.get_rect()
        usernameRect.center = (100, 160)
        #blits to the screen
        signUpWindow.blit(usernameText, usernameRect)
        
        #renders the password title for the sign up page
        passwordFont = pygame.font.Font('freesansbold.ttf', 15)
        passwordText = passwordFont.render("Password:", True, (46, 94, 59), (56, 55, 53))
        passwordRect = passwordText.get_rect()
        passwordRect.center = (100, 260)
        #blits to the screen
        signUpWindow.blit(passwordText, passwordRect)
        
        #if there is an error with the name then give apt failure message
        if failed == "nameError":
            if t.is_alive():
                failure(signUpWindow, f"username taken, please try again with \n new details {round(time.monotonic() - start, 1)}")            
        #if there is an error with the password range then give failure message
        elif failed == "rangeError":
            if t.is_alive():
                failure(signUpWindow, f"length of password is incorrect, must \n be 7-20 characters {round(time.monotonic() - start, 1)}") 
        #refresh the page
        pygame.display.flip()