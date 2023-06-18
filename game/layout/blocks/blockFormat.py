import pygame
import __main__
import os
pygame.init()

import game.layout.componentFormat as componentFormat

class BlockFormat(componentFormat.ComponentFormat):
    """Class to be subclassed to make different types of blocks that can be shown on the Window().

    Inherits from ComponentFormat. 
    """
    
    def __init__(self, x: int, y: int, path: str) -> None:
        """Needs baseclass arguments

        Args:
            x (int): X position.
            y (int): Y position.
            path (str): Path to the image used for graphics.
        """
        super().__init__(x, y)
        
        self.maindir = os.path.dirname(os.path.realpath(__main__.__file__))
        self.imgpath = self.maindir + "/" + path        
        self.img = pygame.image.load(self.imgpath)
        size = self.img.get_rect()
        self.size = (size.w, size.h)
        self.rect = pygame.rect.Rect(self.coords[0], self.coords[1], self.size[0], self.size[1])
        
    def get_collition(self) -> pygame.rect.Rect:
        """Returns the collition of the block."""
        return self.rect
    
    def set_path(self, path: str):
        self.imgpath = self.maindir + "/" + path
        self.img = pygame.image.load(self.imgpath)
        size = self.img.get_rect()
        self.size = (size.w, size.h)
        self.rect = pygame.rect.Rect(self.coords[0], self.coords[1], self.size[0], self.size[1])
            
    def setPos(self, x: int, y: int) -> None:
        """Sets the position of the block.

        Args:
            x (int): New x position.
            y (int): New y position.
        """
        self.coords[0] = x
        self.coords[1] = y
        self.refresh()
    
    def refresh(self) -> None:
        """Refreshes the position of the block.""" 
        self.rect.move(self.coords[0], self.coords[1])
        
    def get_drawinfo(self) -> tuple[pygame.Surface, list[int]]:
        """Returns the information needed to draw the block.
        
        Returns:
            tuple[pygame.Surface, list[int]]: First is the image and then the position. 
        """
        return self.img, self.coords