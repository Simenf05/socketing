import pygame
from abc import ABC, abstractmethod

pygame.init()

import game.layout.componentFormat as componentFormat

class ButtonFormat(componentFormat.ComponentFormat):
    def __init__(self, x: int, y: int, w: int, h: int, text: None | str = None, color_: str | tuple = "white", bgcolor_: str | tuple = "black", fontSize: int=32, width: int=2) -> None:
        
        super().__init__(x, y)
        
        self.size = (w, h)
        self.text = text
        self.width = width
        
        self.color = color_
        self.bgcolor = bgcolor_
        
        self.fontSize = fontSize
        self.font = pygame.font.Font(None, self.fontSize)
        
        self.refresh()

    def get_drawinfo(self):
        self.visualRefresh()
        return self.surface, self.coords
    
    
    def visualRefresh(self):
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        
        self.textSurface = self.font.render(self.text, True, self.color, self.bgcolor)
        
        self.surface.blit(self.textSurface, (self.width, self.width))
        pygame.draw.rect(self.surface, self.color, self.rect, width=self.width)
        
    def refresh(self):
        
        
        if self.text:
            while not self.size[1] - ((self.width + 1) * 2) >= self.font.get_height():
                self.fontSize -= 1
                self.font = pygame.font.Font(None, self.fontSize)
        
        self.visualRefresh()
    
    @abstractmethod
    def action(self, **kwargs): ...
            
    def selected(self):
        self.width += 1
        self.font.bold = True
        
    def deselected(self):
        self.width -= 1
        self.font.bold = False



    
    
        