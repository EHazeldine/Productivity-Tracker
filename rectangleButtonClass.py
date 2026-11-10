import pygame
import sys
pygame.init()
#instantiates the button class
class rectButton:
    #initialises all attributes
    def __init__(self, window, coordinates, colour,
                 textColour, text, textSize, buttonFunction, *args):
        self.window = window
        self.coordiantes = coordinates
        if isinstance(coordinates, pygame.Rect):
            self.rect = coordinates
        else:
            self.rect = pygame.Rect(coordinates)
        self.colour = colour
        self.textColour = textColour
        self.text = text
        self.textSize = textSize
        self.buttonFunction = buttonFunction
        self.args = args

        
    #initialising the draw function
    def draw(self):
        #draws the rectangle
        pygame.draw.rect(self.window, self.colour,
                         self.rect)
        #sets text font
        buttonFont = pygame.font.Font('freesansbold.ttf',
                                      self.textSize)
        #renders the text
        buttonText = buttonFont.render(self.text, True,
                                       (self.textColour), (self.colour))
        #sets text coordinates in the centre of the button
        textRect = buttonText.get_rect()
        #sets the centre of button
        textRect.center = self.rect.center
        #blits the text
        self.window.blit(buttonText, textRect)
    #executes the specific function upon clicking    
    def click(self, event):
        #if quitting then exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if clicked perform the function with number of arguments
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.args:
                    self.buttonFunction(*self.args)
                else:
                    self.buttonFunction()
  
  
  
  
  
  
  
  
  
                    
class imageRectButton:
    #initialises all attributes
    def __init__(self, window, windowColour, coordinates, size, image, buttonFunction, *args):
        self.window = window
        self.windowColour = windowColour
        self.coordinates = coordinates
        self.size = size
        self.buttonFunction = buttonFunction
        self.args = args
        self.rect = pygame.Rect(self.coordinates, self.size)
        self.image = pygame.transform.scale(image, self.size)
        self.imageRect = self.image.get_rect()
        self.imageRect.center = self.rect.center
    #draws the button
    def draw(self):
        #draws the rectange that can be pressed
        pygame.draw.rect(self.window, self.windowColour, self.rect)
        #draws the image on the screen
        self.window.blit(self.image, self.imageRect)
    def click(self, event):
        #if quitting then exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if clicked perform the function with number of arguments
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.imageRect.collidepoint(event.pos):
                if self.args:
                    self.buttonFunction(*self.args)
                else:
                    self.buttonFunction()





class inputBox:
    #initialises attributes
    def __init__(self, window, coordinates, passiveColour, activeColour,
                 colour, textColour, textSize, userText, active, surfaceText):
        self.window = window
        self.coordiantes = coordinates
        if isinstance(coordinates, pygame.Rect):
            self.rect = coordinates
        else:
            self.rect = pygame.Rect(coordinates)
        self.passiveColour = passiveColour
        self.activeColour = activeColour
        self.colour = colour
        self.textColour = textColour
        self.textSize = textSize
        self.userText = userText
        self.active = active
        self.surfaceText = surfaceText
        self.colour = self.passiveColour
        self.font = pygame.font.Font(None, 32)
    #draws button
    def draw(self):
        #draws the rectangle
        pygame.draw.rect(self.window, self.colour,
                         self.rect, 1)
        #draws another smaller rectange inside, making clearing after deleting possible
        pygame.draw.rect(self.window, (56, 55, 53), (self.rect.x+2,
                                                  self.rect.y+2, self.rect.w-4, self.rect.h-4))
        #if there is a user text input, display that text
        if self.surfaceText:
            self.window.blit(self.surfaceText, (self.rect.x + 5, self.rect.y + 5))
    #when clicked, activate it, changing the colour and allowing typing
    def activate(self):
        self.active = True
        self.colour = self.activeColour
        self.draw()
        pygame.display.flip()
    #when anywhere else is clicked, deactivate it and dont allow typing and refresh display
    def deactivate(self):
        self.active = False
        self.colour = self.passiveColour
        self.draw()
        pygame.display.flip()
    #when a latter is types then append the string and change the size, display the change
    def typing(self, character):
        self.userText += character
        self.surfaceText = self.font.render(self.userText, True, (self.textColour))
        self.window.blit(self.surfaceText, self.rect)
        self.rect.w = max(300, self.surfaceText.get_width()+10)
    #when backspace pressed then remove the last letter and change the size
    def delete(self):
        self.userText = self.userText[:-1]
        self.surfaceText = self.font.render(self.userText, True, self.textColour)