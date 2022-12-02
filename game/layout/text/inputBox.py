import pygame
import time
pygame.init()

import game.layout.componentFormat as componentFormat

# keys that the inputbox will register
# can be overridden
keyboard = [
    pygame.K_a,
    pygame.K_b,
    pygame.K_c,
    pygame.K_d,
    pygame.K_e,
    pygame.K_f,
    pygame.K_g,
    pygame.K_h,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_m,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_q,
    pygame.K_r,
    pygame.K_s,
    pygame.K_t,
    pygame.K_u,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z,
    pygame.K_0,
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
    pygame.K_SPACE,
    pygame.K_PERIOD
]


class InputBox(componentFormat.ComponentFormat):
    """Inputbox to type in.

    Inherits from ComponentFormat.
    """
    
    def __init__(self, x: int, y: int, w: int, h: int, text: str="", color_: str | tuple= "white", bgcolor_: str | tuple= "black", fontSize: int = 32, timeDiff: float=.2, backspaceTimeDiff: float=.1, width: int=2) -> None:
        """Sets up all the timing for the keys and color.

        Args:
            x (int): X position.
            y (int): Y position.
            w (int): Width.
            h (int): Height.
            text (str, optional): Standard text in the inputbox. Defaults to "".
            color_ (str | tuple, optional): Color of the inputbox, can be rgb tuple or pygame color string. Defaults to "white".
            bgcolor_ (str | tuple, optional): Background color of inputbox, can be rgb or pygame color string. Defaults to "black".
            fontSize (int, optional): Fontsize that will shrink depending on the size of the inputbox. Defaults to 32.
            timeDiff (float, optional): Time between key reistration. Defaults to .2.
            backspaceTimeDiff (float, optional): Time between backspace registration. Defaults to .1.
            width (int, optional): Width of the border around the inputbox. Defaults to 2.
        """
        
        super().__init__(x, y)
        
        self.fontSize = fontSize 
        self.font = pygame.font.Font(None, self.fontSize)
        
        self.color = color_
        self.bgcolor = bgcolor_
        
        self.size = (w, h)
        self.text = text
        self.selectLine = False
        self.width = width
        
        
        self.lineTime = round(time.time())
        self.nowTime = time.time()
        self.timeDiff = timeDiff
        self.backspaceDiff = backspaceTimeDiff
        self.lastTime = {}
        self.backspaceLastTime = self.nowTime
        
        for key in keyboard:
            self.lastTime.update({pygame.key.name(key): self.nowTime})
        
        self.refresh()
        
    def get_drawinfo(self) -> tuple[pygame.Surface, list[int]]:
        """Returns the information needed to blit the inputbox.

        Returns:
            tuple[pygame.Surface, list[int]]: First is the pygame surface and then the position. 
        """
        self.lineTime = round(time.time())
        self.visualRefresh()
        return self.surface, self.coords
    
    
    def visualRefresh(self) -> None:
        """Updates all the visual elements of the inputbox."""
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        
        self.textSurface = self.font.render(self.text, True, self.color, self.bgcolor)
        textRect = self.textSurface.get_rect()
        
        if self.selectLine:
            if self.lineTime % 2 == 0:
                pygame.draw.line(self.surface, self.color, (textRect.x + textRect.w + (self.width * 2), textRect.y + self.width), (textRect.x + textRect.w + (self.width * 2), textRect.x + textRect.h - self.width))
            
        self.surface.blit(self.textSurface, (self.width, self.width))
        pygame.draw.rect(self.surface, self.color, self.rect, width=self.width)
    
    
    def refresh(self):
        """Refreshes the font size and visuals."""
        self.nowTime = time.time()
        
        if self.text:
            while not self.size[1] - ((self.width + 1) * 2) >= self.font.get_height():
                self.fontSize -= 1
                self.font = pygame.font.Font(None, self.fontSize)
        
        self.visualRefresh()
    
    
    def getText(self) -> str:
        """Get the text present in the inputbox.

        Returns:
            str: The text in the box.
        """
        return str(self.text)
    
    def changeText(self, newText: str) -> None:
        """Changes the text in the inputbox.

        Args:
            newText (str): The new text.
        """
        self.text = newText
        self.refresh()
    
    def action(self, **kwargs) -> None:
        """Action performed every frame to check if it was pressed."""
        self.nowTime = time.time()
        
        if kwargs["pressed"][pygame.K_BACKSPACE]:
            if (self.nowTime - self.backspaceLastTime > self.backspaceDiff):
                self.changeText(self.text[:-1])
                self.backspaceLastTime = self.nowTime
        
        for key in keyboard:
            if kwargs["pressed"][key]:
                if (self.nowTime - self.lastTime[pygame.key.name(key)] > self.timeDiff):
                    if pygame.key.name(key) == "space":
                        self.changeText(self.text + " ")
                    else:
                        if kwargs["pressed"][pygame.K_LSHIFT] or kwargs["pressed"][pygame.K_RSHIFT]:
                            self.changeText(self.text + pygame.key.name(key).capitalize())
                        
                        else:
                            self.changeText(self.text + pygame.key.name(key))
                    self.lastTime[pygame.key.name(key)] = self.nowTime
                    
    def selected(self) -> None:
        """Sets the inputbox to be selected."""
        self.width += 1
        self.selectLine = True
        
    def deselected(self) -> None:
        """Sets the inputbox to be deselected."""
        self.width -= 1
        self.selectLine = False
        
    def __str__(self) -> str:
        """The string form of the object.

        Returns:
            str: Text of the inputbox.
        """
        return str(self.text)
    