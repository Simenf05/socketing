from typing import Any
class Layout:
    """Layout to keep order over the components and select them with the arrows."""
    
    def __init__(self, dimensions: tuple, objList: None | list = None, start: tuple = (1, 1), fillerValue: Any = None) -> None:
        """Creats the layout and fills the empty spots.

        Args:
            dimensions (tuple): Dimentions of the layout.
            objList (None | list, optional): Optional list of objects to auto-fill in. Defaults to None.
            start (tuple, optional): Set the start position. Defaults to (1, 1).
            fillerValue (Any, optional): This should be None. Defaults to None.
        """
        
        self.grid = []
        self._pos = [start[0], start[1]]
        self.dim = dimensions
        self.selected = None
        self.fillerValue = fillerValue
        
        for col in range(self.dim[0]):
            self.grid.append([])
        
        for row in self.grid:
            for i in range(self.dim[1]):
                row.append(self.fillerValue)
        
        if objList:
            for objAndPos in objList:
                self.setValue(objAndPos[1], objAndPos[2])
            
            self.selected = self.updateSelected(start)
        
        
    
    def setValue(self, obj: object, pos: tuple) -> None:
        """Sets the object in a position of the layout.

        NOTE: The first object in the layout has pos (1, 1).

        Args:
            obj (object): Object to set in, should inherit from ComponentFormat.
            pos (tuple): Position to place.

        Raises:
            IndexError: The position can not be 0.
        """
        
        if pos[0] == 0 or pos[1] == 0:
            raise IndexError("Pos cannot be 0")
        self.grid[pos[0] - 1][pos[1] - 1] = obj     
        
        
    def updateSelected(self, newPos: tuple) -> object:
        """Selects the position and deselects that last selection.

        Args:
            newPos (tuple): The position of the new object to be selected.

        Returns:
            object: Returns the new selected object.
        """
        
        self.grid[self._pos[0] - 1][self._pos[1] - 1].deselected()        
        self.grid[newPos[0] - 1][newPos[1] - 1].selected()
        
        return self.grid[newPos[0] - 1][newPos[1] - 1]
    
    def doAction(self, **kwargs) -> None:
        """Does the action() of the current position."""
        self.grid[self._pos[0] - 1][self._pos[1] - 1].action(**kwargs)
    
    def updatePos(self, newPos: tuple) -> None:
        """Moves to a new position and selects that position.

        Args:
            newPos (tuple): New position to move to.

        Raises:
            IndexError: If the new pos is out of range on x.
            IndexError: If the new pos is out of range on y.
        """
        
        if newPos[0] < 1 or newPos[0] > self.dim[0]:
            raise IndexError(f"Value {newPos[0]} out of grid range")
        
        if newPos[1] < 1 or newPos[1] > self.dim[1]:
            raise IndexError(f"Value {newPos[1]} out of grid range")
        
        if self.grid[newPos[0] - 1][newPos[1] - 1] == None:
            return
        
        self.selected = self.updateSelected(newPos)
        self._pos = [newPos[0], newPos[1]]
        
    def getPos(self) -> list[int]:
        """Returns the position.

        Returns:
            list: First the x pos and then the y pos.
        """
        return self._pos.copy()
    
    def __str__(self) -> str:
        """Retruns the string form of the object.

        Returns:
            str: Values from the layout.
        """
        
        grid = self.grid.copy()
        string = ""
        
        string += "["
        
        for col in grid:
            if col is grid[-1]:
                string += str(col)
            else:
                string += str(col) + ",\n"
        
        string += "]"
        return string
    


if __name__ == "__main__":
    
    list = [("heisann", (2, 2)), 
            ("hvordan gar dagen din da", (1, 1)),
            ("haper den gar bra :)", (4, 4))
            ]

    layout = Layout((10, 10), list)

    print(layout)