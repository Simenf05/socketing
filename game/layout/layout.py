
class Layout:
    def __init__(self, dimensions: tuple, objList=None, start: tuple= (1, 1), fillerValue=None) -> None:
        
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
        
        
    
    def setValue(self, obj, pos: tuple) -> None:
        
        if pos[0] == 0 or pos[1] == 0:
            raise IndexError("Pos cannot be 0")
        self.grid[pos[0] - 1][pos[1] - 1] = obj     
        
        
    def updateSelected(self, newPos: tuple) -> None:
        
        self.grid[self._pos[0] - 1][self._pos[1] - 1].deselected()        
        self.grid[newPos[0] - 1][newPos[1] - 1].selected()
        
        return self.grid[newPos[0] - 1][newPos[1] - 1]
    
    def doAction(self, **kwargs):
        self.grid[self._pos[0] - 1][self._pos[1] - 1].action(**kwargs)
    
    def updatePos(self, newPos: tuple) -> None:
        
        if newPos[0] < 1 or newPos[0] > self.dim[0]:
            raise IndexError(f"Value {newPos[0]} out of grid range")
        
        if newPos[1] < 1 or newPos[1] > self.dim[1]:
            raise IndexError(f"Value {newPos[1]} out of grid range")
        
        if self.grid[newPos[0] - 1][newPos[1] - 1] == None:
            return
        
        self.selected = self.updateSelected(newPos)
        self._pos = [newPos[0], newPos[1]]
        
    def getPos(self) -> list:
        return self._pos.copy()
    
    def __str__(self) -> str:
        
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