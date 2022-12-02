from abc import ABC, abstractmethod

class ComponentFormat(ABC):
    """Class to be subclassed to create objects that can be shown on the Window().
    
    Inherits from ABC.
    """
    
    def __init__(self, x: int, y: int) -> None:
        """All components need x and y.

        Args:
            x (int): X position.
            y (int): Y position.
        """
        self.coords = [x, y]
    
    # override these functions to add funcionality
    def selected(self): ...
    def deselected(self): ...
    def refresh(self): ...
    @abstractmethod
    def get_drawinfo(self): ...
    def action(self, **kwargs): ...
    