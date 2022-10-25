
class Layout:
    def __init__(self, dimensions: tuple, objList=None, hori=False) -> None:
        
        self.grid = []
        self.pos = [1, 1]
        
        for col in range(dimensions[0]):
            self.grid.append([])
        
        
        
        for row in self.grid:
            for i in range(dimensions[1]):
                row.append(None)
        
        if objList:
            for objAndPos in objList:
                self.setValue(objAndPos[0], objAndPos[1])

    
    def setValue(self, obj, pos: tuple):
        
        if pos[0] == 0 or pos[1] == 0:
            raise IndexError("Pos cannot be 0")
        self.grid[pos[0] - 1][pos[1] - 1] = obj     
        
    
    def keypress(self, key):
        
        
        
        print(key)
        pass
    
    def __repr__(self) -> str:
        
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