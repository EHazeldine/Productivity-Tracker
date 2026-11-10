#importing any relevant libraries/functions
import pygame
import sqlite3
import sys
import time
import threading
pygame.init()
from logInFunction import logIn
from startPage import startPage
from checkUserData import checkLogIn
from signUpFunction import signUp
from rectangleButtonClass import rectButton
from mainPage import mainPage
from Leaderboard import leaderboard
from customisePage import customisePage
#the program always begins with the start screen so currentScreen must be initialised as such
currentScreen = "start"
currentUser = ""
#default failures are false
failed = False
#sets infinite game loop
running = True
while running:
    #if we are on the start page, the result from the start page is the output from the start function
    if currentScreen == "start":
        result = startPage()
    #if we are on the log in page, the result from log in is the output from the login function
    elif currentScreen == "login":
        result = logIn(failed)
    #if we are on the sign up page, the result from this is the output from the sign up function
    elif currentScreen == "signUp":
        result = signUp(failed)
    #if on the main page, the result from this is the output from the main page function
    elif currentScreen == "main Page":
        result = mainPage(currentUser, failed)
    #if on the leaderboard page, result from this is the leaderboard function
    elif currentScreen == "leaderboard":
        result = leaderboard(currentUser)
    #if on the customise page, result from this is the customisePage function
    elif currentScreen == "customise Page":
        result = customisePage(currentUser)
    
    #if the returned result is a tuple...
    if isinstance(result, tuple):
        #if length is 2
        if len(result) == 2:
            #set the first to nextScreen and next to username
            nextScreen, username = result
            result = nextScreen
            #sets the current user to the returned username
            if username:
                currentUser = username
        #if length is 3
        elif len(result) == 3:
            #sets first to next screen, second to username and third to failed
            nextScreen, username, failed = result
            
    #if any function returns "logIn", it will go to the login page (can happen at several points)
    if result == "logIn":
        currentScreen = "login"
    #if any function returns "start", it will go to the start page (either back buttons from signUp/logIn pages)
    elif result == "start":
        currentScreen = "start"
    #if any function returns "sign up", it will go to the sign up page (also happens at several points)
    elif result == "signUp":
        currentScreen = "signUp"
    #if any function returns "main Page" it will go to the main page
    elif result == "main Page":
        currentScreen = "main Page"
    #if any function returns "refreshHome" it will go back to an updated main page
    elif result == "refreshHome":
        currentScreen = "main Page"
    #if any function returns "leaderboard page" it will go to the leaderboard page
    elif result == "leaderboard Page":
        currentScreen = "leaderboard"
    #if any function returns "customise page" it will go to the customise page
    elif result == "customise Page":
        currentScreen = "customise Page"
    #if we do not get a result then stop the game loop
    elif result is None:
        running = False 
pygame.quit()