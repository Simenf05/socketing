import pygame
pygame.init()

from . import actionWall

class NextScreenBlck(actionWall.ActionWall):
    
    def __init__(self, x: int, y: int, path: str, screen, newScreen: str, newCoords: tuple) -> None:
        super().__init__(x, y, path)
        
        self.screen = screen
        self.newScreen = newScreen
        self.newCoords = newCoords
        
    def action(self, **kwargs): 
        self.screen.setOnScreen(self.newScreen)
        self.screen.screenDict[self.screen.onScreen].player.setPos(self.newCoords[0], self.newCoords[1])