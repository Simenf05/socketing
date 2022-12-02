import pygame
pygame.init()

from . import map as mp

class Window:
    """Makes and manages window"""
    def __init__(self, screensize: tuple, onScreen=None, screenName="screen", dict: dict={}) -> None:
        
        self.screenName = screenName
        self.onScreen = onScreen
        
        self.screenDict = {}
        
        self.screen = pygame.display.set_mode(screensize)
        self.clock = pygame.time.Clock()
        
        
        
        if dict:
            for key, value in dict.items():
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
        
        # print(self.screenDict)
        
        self.screenDict[self.onScreen].drawAll(self.screen)
        
        pygame.display.update()
        self.clock.tick(30)
        
        
    def keypressReg(self, keysPressed):
        self.screenDict[self.onScreen].action(pressed=keysPressed)
    
    def addPlayerToAllMaps(self, key: str, obj):
        for map in self.screenDict.values():
            if type(map) == mp.Map:
                map.addOPlayer(key, obj)
    
    def __str__(self) -> str:
        string = ""
        string += "Screen: " + str(self.screen) + "\n"
        string += "On Screen: " + str(self.onScreen) + "\n"
        string += "Dict: " + str(self.screenDict)
        return string

