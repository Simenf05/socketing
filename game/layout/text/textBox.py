import pygame.font
pygame.font.init()

import game.layout.componentFormat as componentFormat

class TextBox(componentFormat.ComponentFormat):
    """Textbox to show text in.

    Inherits from ComponentFormat.
    """
    def __init__(self, x: int, y: int, text: str, color_: str | tuple= "white", fontObj: pygame.font.Font = pygame.font.Font(None, 32)) -> None:
        """Sets up the text and color.

        Args:
            x (int): X position.
            y (int): Y position.
            text (str): The text to show.
            color_ (str | tuple, optional): Color of the textbox, can be rgb tuple or pygame color string. Defaults to "white".
            fontObj (pygame.font.Font, optional): Fontsize that will shrink depending on the size of the textbox. Defaults to pygame.font.Font(None, 32).
        """
        
        super().__init__(x, y)
        
        self.font = fontObj
        self.color = color_
        self.text = text
        
        self.refresh()
        
    
    def get_drawinfo(self) -> tuple[pygame.Surface, list[int]]:
        """Returns the needed to blit the textbox.

        Returns:
            tuple[pygame.Surface, list[int]]: First is the pygame surface and then the position. 
        """
        return self.textSurface, self.textRect
    
    def refresh(self) -> None:
        """Refreshes the font size and visuals."""
        self.textSurface = self.font.render(self.text, True, self.color, "black")
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = self.coords
        
    def selected(self) -> None:
        """Sets the textbox to be selected."""
        self.color = "blue"
        self.font.bold = True
        self.refresh()
        
    def deselected(self) -> None:
        """Sets the textbox to be deselected."""
        self.color = "red"
        self.font.bold = False
        self.refresh()
    
    def __str__(self) -> str:
        """Retruns the string form of the object.

        Returns:
            str: Text of the textbox.
        """
        return str(self.text)
    
if __name__ == "__main__":
    txt = TextBox(1, 2, "hei", "red")    
    
    print(txt)