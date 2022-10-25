import pygame.font
pygame.font.init()

class TextBox:
    def __init__(self, x: int, y: int, text: str, color_, fontObj: pygame.font.Font = pygame.font.Font(None, 32)) -> None:
        
        self.font = fontObj
        
        self.text = text
        
        self.textObj = self.font.render(text, True, color_, "black")
        
        self.textRect = self.textObj.get_rect()
        self.textRect.center = (x, y)
    
    def get_drawinfo(self):
        return self.textObj, self.textRect
        
    def selected(self):
        pass
    
    def unselected(self):
        pass
    
    def __repr__(self) -> str:
        return self.text
    
if __name__ == "__main__":
    txt = TextBox(1, 2, "hei", "red")
    
    
    
    print(txt)