#import and initialise libraries
import pygame
import time
import threading
pygame.init()
def failure(window, displayText):
    #draws rectangles at the top of the screen
    alertRect = pygame.Rect(150, 0, 300, 50)
    pygame.draw.rect(window, (56, 55, 53), alertRect)
    pygame.draw.rect(window, (46, 94, 59), alertRect, 2)
    textPrevious = 0
    #sets the font
    failureMessageFont = pygame.font.Font('freesansbold.ttf', 15)
    #split into lines whenever \n is encountered
    lines = displayText.split('\n')
    #each new line is 10 pixels down
    y = 10
    #renders text on the screen
    for line in lines:
        text_surface = failureMessageFont.render(line, True, (46, 94, 59))
        window.blit(text_surface, (155, y))
        y += failureMessageFont.get_linesize()

def runningTime(function, duration, window):
    #while the alert is running, sleep every 0.1 to reduce load
    start = time.monotonic()
    while time.monotonic() - start < duration:
        time.sleep(0.1)