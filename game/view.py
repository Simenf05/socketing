

class View:
    """Class to be subclassed to create objects that can contain derived objects of ComponentFormat().
    """
    def __init__(self, drawing: dict, layout) -> None:
        
        self.drawing = {}
        self.layout = layout
        
        if drawing:
            for key, value in drawing.items():
                self.drawing.update({key: value})
        
        
    def addDraw(self, newDraw: tuple[str, object] | dict) -> None:
        """Adds a new object to the drawing dictionary.

        Args:
            newDraw (tuple[str, object] | dict): If tuple then the first should be key and then the object. If dict then {key : value} pairs.
        """
        if type(newDraw) is dict:
            for key, value in newDraw.items():
                self.drawing.update({key: value})

        else:
            self.drawing.update({str(newDraw[0]): newDraw[1]})
    
    
    def popDraw(self, key: str) -> None:
        """Removes the key from drawing dictionary.

        Args:
            key (str): Key of object to remove.
        """
        self.drawing.pop(key)
    
    
    def drawAll(self, screen_: object) -> None:
        """Draws all the components in the drawing dictionary.

        Args:
            screen_ (object): Main Window() object.
        """        
        
        for obj in self.drawing.values():
            
            obj, rect = obj.get_drawinfo()
            screen_.blit(obj, rect)
    
    
    def draw(self, key: str) -> None:
        """Draws the one key from the drawing dictionary.

        Args:
            key (str): The key that should be drawn.
        """        
        self.drawing[key].drawSelf()
        
        
    def action(self, **kwargs): ...
        # This one should be overridden.
        
    def __str__(self) -> str:
        """Returns the string form of the class."""    
        return "Drawing dict: " + str(self.drawing)

