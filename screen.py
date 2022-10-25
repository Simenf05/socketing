import pygame
pygame.init()


class Screen:
    def __init__(self, screensize: tuple, onScreen=None, screenName="screen", dict: dict={}) -> None:
        
        self.screenName = screenName
        self.onScreen = onScreen
        
        self.screenDict = {}
        
        self.screen = pygame.display.set_mode(screensize)
        self.clock = pygame.time.Clock()
        
        self.BIGFONT = pygame.font.Font(None, 52)
        self.NORMALFONT = pygame.font.Font(None, 42)
        self.SMALLFONT = pygame.font.Font(None, 32)
        
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        
        if dict:
            for key, value in dict.items():
                print("setting values")
                self.screenDict.update({key: value})
    
    
    def addScreen(self, newScreen, changeScreen: bool=False):
        if type(newScreen) is dict:
            for key, value in newScreen.items():
                self.screenDict.update({key: value})

        else:
            self.screenDict.update({str(newScreen[0]): newScreen[1]})
            if changeScreen:
                self.onScreen = str(newScreen[0])
        
        
    def setOnScreen(self, onScreen: str):
        self.onScreen = onScreen


    def popScreen(self, key: str):
        self.screenDict.pop(key)
        
        
    def updateScreen(self):
        self.screen.fill("black")
        
        self.screenDict[self.onScreen].drawAll(self.screen)
        
        pygame.display.update()
        self.clock.tick(30)
        
        
    def keypressReg(self, pressed):
        self.screenDict[self.onScreen].action(pressed)
        
    
    def __repr__(self) -> str:
        string = ""
        string += "Screen: " + str(self.screen) + "\n"
        string += "On Screen: " + str(self.onScreen) + "\n"
        string += "Dict: " + str(self.screenDict)
        return string

