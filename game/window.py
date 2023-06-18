import pygame
from typing import Sequence
pygame.init()

from . import map as mp

class Window:
    """Main class that makes and manages pygame window."""
    def __init__(self, screensize: tuple, onScreen: str | None = None, screenName: str = "screen", viewDict: dict = {}) -> None:
        """Sets up the screenDict and onScreen.

        Args:
            screensize (tuple): Size of the pygame window.
            onScreen (str | None, optional): String of the key to the subclass of View() to show, if None you will have to set it later. Defaults to None.
            screenName (str, optional): Name of the window object. Defaults to "screen".
            viewDict (dict, optional): Dictionary containing all the subclasses of View() to show and corresponding key. Defaults to {}.
        """
        self.screenName = screenName
        self.onScreen = onScreen
        
        self.screenDict = {}
        
        self.screen = pygame.display.set_mode(screensize)
        self.clock = pygame.time.Clock()
        
        if viewDict:
            for key, value in viewDict.items():
                self.screenDict.update({key: value})
    
    
    def addScreen(self, newScreen: tuple[str, object] | dict, changeScreen: bool=False) -> None:
        """Adds a new object to the viewDict dictionary.

        Args:
            newScreen (tuple[str, object] | dict): If tuple then the first should be key and then the View() subclass. If dict then {key : value} pairs.
            changeScreen (bool, optional): If the new screen should be set as onScreen. Defaults to False.
        """
        if type(newScreen) is dict:
            for key, value in newScreen.items():
                self.screenDict.update({key: value})

        else:
            self.screenDict.update({str(newScreen[0]): newScreen[1]})
            if changeScreen:
                self.onScreen = str(newScreen[0])
        
        
    def setOnScreen(self, onScreen: str) -> None:
        """Sets new key for the View() subclass on screen.

        Args:
            onScreen (str): The new key.
        """
        self.onScreen = onScreen


    def popScreen(self, key: str) -> None:
        """Removes a Veiw() subclass from veiwDict.

        Args:
            key (str): The key to remove.
        """
        self.screenDict.pop(key)
        
        
    def updateScreen(self) -> None:
        """Updates the drawings on the screen.
        Should be called every frame."""
        
        self.screen.fill("black")
        
        self.screenDict[self.onScreen].drawAll(self.screen)
        
        pygame.display.update()
        self.clock.tick(30)
        
        
    def keypressReg(self, keysPressed: Sequence[bool]) -> None:
        """Does the action for the View() subclass on screen. 

        Args:
            keysPressed (Sequence[bool]): Should be the return of pygame.key.get_pressed().
        """

        self.screenDict[self.onScreen].action(pressed=keysPressed)
    
    def addPlayerToAllMaps(self, key: str, obj: object) -> None:
        """Adds players to all the Map() objects.

        Args:
            key (str): The key of the player.
            obj (object): The player object.
        """
        for map in self.screenDict.values():
            if type(map) == mp.Map:
                map.addOPlayer(key, obj)
    
    def __str__(self) -> str:
        """Returns the string form of the object.

        Returns:
            str: Screen name, pygame screen object, on screen value, screenDict with all the View() subclasses.
        """
        string = ""
        string += "Name: " + str(self.screenName) + "\n"
        string += "Screen: " + str(self.screen) + "\n"
        string += "On Screen: " + str(self.onScreen) + "\n"
        string += "Dict: " + str(self.screenDict)
        return string

