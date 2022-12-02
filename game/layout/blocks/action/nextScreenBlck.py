import pygame
pygame.init()

from . import actionWall

class NextScreenBlck(actionWall.ActionWall):
    """Wall that will take you to the next screen.

    Inherits from ActionWall
    """
    
    def __init__(self, x: int, y: int, path: str, screen, newScreen: str, newCoords: tuple) -> None:
        """Initializes the block.

        Args:
            x (int): X position.
            y (int): Y position.
            path (str): Path to the image used for graphics.
            screen (_type_): The Window object.
            newScreen (str): The new value to set Window.onScreen.
            newCoords (tuple): The new coordinates to set the player to.
        """
        super().__init__(x, y, path)
        
        self.screen = screen
        self.newScreen = newScreen
        self.newCoords = newCoords
        
    def action(self, **kwargs) -> None:
        """The action performed when the player contacts the block."""
        self.screen.setOnScreen(self.newScreen)
        self.screen.screenDict[self.screen.onScreen].player.setPos(self.newCoords[0], self.newCoords[1])