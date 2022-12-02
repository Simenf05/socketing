import pygame
from abc import abstractmethod

pygame.init()

import game.layout.componentFormat as componentFormat

class ButtonFormat(componentFormat.ComponentFormat):
    """Class to be subclassed to make different types buttons that can be clicked.

    Inherits from ComponentFormat.
    """
    
    def __init__(self, x: int, y: int, w: int, h: int, text: None | str = None, color_: str | tuple = "white", bgcolor_: str | tuple = "black", fontSize: int=32, width: int=2) -> None:
        """Initializes the button with size and position. 

        Args:
            x (int): X position.
            y (int): Y position.
            w (int): Width.
            h (int): Hight. 
            text (None | str, optional): The text on the button. Defaults to None.
            color_ (str | tuple, optional): Color of the button, can be rgb tuple or pygame color string. Defaults to "white".
            bgcolor_ (str | tuple, optional): Background color of button, can be rgb or pygame color string. Defaults to "black".
            fontSize (int, optional): Fontsize that will shrink depending on the size of the button. Defaults to 32.
            width (int, optional): Width of the border around the button. Defaults to 2.
        """
        
        super().__init__(x, y)
        
        self.size = (w, h)
        self.text = text
        self.width = width
        
        self.color = color_
        self.bgcolor = bgcolor_
        
        self.fontSize = fontSize
        self.font = pygame.font.Font(None, self.fontSize)
        
        self.refresh()

    def get_drawinfo(self) -> tuple[pygame.Surface, list[int]]:
        """Returns the information needed to draw the button.

        Returns:
            tuple[pygame.Surface, list[int]]: First is the pygame surface and then the position. 
        """
        self.visualRefresh()
        return self.surface, self.coords
    
    
    def visualRefresh(self) -> None:
        """Updates the visual aspect of the button."""
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        
        self.textSurface = self.font.render(self.text, True, self.color, self.bgcolor)
        
        self.surface.blit(self.textSurface, (self.width, self.width))
        pygame.draw.rect(self.surface, self.color, self.rect, width=self.width)
        
    def refresh(self) -> None:
        """Refreshes the font size and visuals."""
        if self.text:
            while not self.size[1] - ((self.width + 1) * 2) >= self.font.get_height():
                self.fontSize -= 1
                self.font = pygame.font.Font(None, self.fontSize)
        
        self.visualRefresh()
    
    @abstractmethod
    def action(self, **kwargs): ...
        
    def selected(self) -> None:
        """Sets the button to be selected."""
        self.width += 1
        self.font.bold = True
        
    def deselected(self) -> None:
        """Sets the button to be deselected."""
        self.width -= 1
        self.font.bold = False



    
    
        