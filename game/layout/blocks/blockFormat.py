import pygame
import __main__
import os
pygame.init()

import game.layout.componentFormat as componentFormat

class BlockFormat(componentFormat.ComponentFormat):
    
    def __init__(self, x: int, y: int, path: str) -> None:
        super().__init__(x, y)
        
        self.maindir = os.path.dirname(os.path.realpath(__main__.__file__))
        self.imgpath = self.maindir + "/" + path        
        self.img = pygame.image.load(self.imgpath)
        size = self.img.get_rect()
        self.size = (size.w, size.h)
        self.rect = pygame.rect.Rect(self.coords[0], self.coords[1], self.size[0], self.size[1])
        
    def get_collition(self) -> pygame.rect.Rect:
        return self.rect
    
    def setPos(self, x, y):
        self.coords[0] = x
        self.coords[1] = y
        self.refresh()
    
    def refresh(self):        
        self.rect.move(self.coords[0], self.coords[1])
        
    def get_drawinfo(self):
        return self.img, self.coords