import game.layout.button.buttonFormat as buttonFormat
from pygame import K_RETURN

class NextScreenAndConnBtn(buttonFormat.ButtonFormat):
    """Button that takes you to a different screen and starts connection.

    Inherits from ButtonFormat.
    """
    def __init__(self, x: int, y: int, w: int, h: int, game, newScreen: str, text: None | str = None, activeButton: int = K_RETURN, color_: str | tuple = "white", bgcolor_: str | tuple = "black", fontSize: int = 32, width: int = 2) -> None:
        """Initilaizes the button.

        Args:
            x (int): X position.
            y (int): Y position.
            w (int): Width.
            h (int): Height.
            screen (Window): The main Window object.
            newScreen (str): Name of the new screen.
            text (None | str, optional): Text on the button. Defaults to None.
            activeButton (int, optional): Key to press the button. Defaults to K_RETURN.
            color_ (str | tuple, optional): Color of the button, can be rgb tuple or pygame color string. Defaults to "white".
            bgcolor_ (str | tuple, optional): Background color of button, can be rgb or pygame color string. Defaults to "black".
            fontSize (int, optional): Fontsize that will shrink depending on the size of the button. Defaults to 32.
            width (int, optional): Width of the border around the button. Defaults to 2.
        """
        super().__init__(x, y, w, h, text, color_, bgcolor_, fontSize, width)

        self.game = game
        self.newScreen = newScreen
        self.activeButton = activeButton
        
    def action(self, **kwargs):
        """Takes you to the next screen."""
        
        if kwargs["nowTime"] - kwargs["actionLast"] > kwargs["timeDiff"]:
            if kwargs["pressed"][self.activeButton]:
                
                host = self.game.mainwindow.screenDict["start"].drawing["input_ip"].getText()
                port = 8069
                
                try:
                    self.game.connect_to_server(host, port)
                
                except Exception as e:
                    print(e)
                    return
                
                self.game.mainwindow.setOnScreen(self.newScreen)
            