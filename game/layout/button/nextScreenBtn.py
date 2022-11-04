import game.layout.button.buttonFormat as buttonFormat
from pygame import K_RETURN

class NextScreen(buttonFormat.ButtonFormat): 
    def __init__(self, x: int, y: int, w: int, h: int, screen, newScreen: str, text: None | str = None, color_: str | tuple = "white", bgcolor_: str | tuple = "black", fontSize: int = 32, width: int = 2) -> None:
        super().__init__(x, y, w, h, text, color_, bgcolor_, fontSize, width)

        self.screen = screen
        self.newScreen = newScreen
        
    def action(self, **kwargs):
        
        if kwargs["nowTime"] - kwargs["actionLast"] > kwargs["timeDiff"]:
            if kwargs["pressed"][K_RETURN]:
                self.screen.setOnScreen(self.newScreen)