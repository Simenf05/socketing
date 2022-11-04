import pygame.font
pygame.font.init()

import game.layout.componentFormat as componentFormat

class TextBox(componentFormat.ComponentFormat):
    def __init__(self, x: int, y: int, text: str, color_, fontObj: pygame.font.Font = pygame.font.Font(None, 32)) -> None:
        
        super().__init__(x, y)
        
        self.font = fontObj
        self.color = color_
        self.text = text
        
        self.refresh()
        
    
    def get_drawinfo(self):
        return self.textSurface, self.textRect
    
    def refresh(self):
        self.textSurface = self.font.render(self.text, True, self.color, "black")
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = self.coords
        
    def selected(self):
        self.color = "blue"
        self.font.bold = True
        self.refresh()
        
    def deselected(self):
        self.color = "red"
        self.font.bold = False
        self.refresh()
    
    def __str__(self) -> str:
        return str(self.text)
    
if __name__ == "__main__":
    txt = TextBox(1, 2, "hei", "red")    
    
    print(txt)