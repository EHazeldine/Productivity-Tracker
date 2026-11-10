#imports and initialises all classes and libraries
import sqlite3
import pygame
from rectangleButtonClass import rectButton
pygame.init()
def startPage():
    #sets empty function for the enter button
    def enter():
        pass
    #creates the startWindow with dimensions and names it 'Start Page'
    startWindow = pygame.display.set_mode((600, 600))
    #creates the background colour and clock
    background = (56, 55, 53)
    clock = pygame.time.Clock()
    #sets up the sign up button which sends users to sign up page
    signUpButton = rectButton(startWindow, 
            pygame.Rect(150, 350, 300, 75),
            pygame.Color(46, 94, 59),
            pygame.Color(56, 55, 53),
            "Sign Up", 32, enter)
    #sets up the log i nbutton which sends users to log in page
    logInButton = rectButton(startWindow, 
            pygame.Rect(150, 450, 300, 75),
            pygame.Color(46, 94, 59),
            pygame.Color(56, 55, 53),
            "Log In", 32, enter)
    #sets infinite loop
    running = True
    while running:
        #fills window with background colour
        startWindow.fill(background)

        #draws the buttons
        signUpButton.draw()
        logInButton.draw()
        
        #draws the title for the page
        titleFont = pygame.font.Font('freesansbold.ttf', 50)
        titleText = titleFont.render("Productivity Tracker", True, (46, 94, 59), (56, 55, 53))
        titleRect = titleText.get_rect()
        titleRect.center = (300, 200)
        #blits to the screen
        
        startWindow.blit(titleText, titleRect)
        for event in pygame.event.get():
            #if we want to quit then quit
            if event.type == pygame.QUIT:
                running = False
            #when we click, depending on the location of the mouse, either log in or sign up
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if clicked on top of the sign up button, go to sign up function
                if signUpButton.rect.collidepoint(event.pos):
                    return "signUp"
                #if clicked on top of the log in button, go to log in function
                elif logInButton.rect.collidepoint(event.pos):
                    return "logIn"
        #refresh the display
        pygame.display.flip()