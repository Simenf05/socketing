

class ScreenFormat:
    def __init__(self, drawing: dict, layout) -> None:
        
        self.drawing = {}
        self.layout = layout
        
        if drawing:
            for key, value in drawing.items():
                self.drawing.update({key: value})
        
    
    def addDraw(self, newDraw):
        if type(newDraw) is dict:
            for key, value in newDraw.items():
                self.drawing.update({key: value})

        else:
            self.drawing.update({str(newDraw[0]): newDraw[1]})
    
    
    def popDraw(self, key: str):
        self.drawing.pop(key)
    
    
    def drawAll(self, screen_):
        
        for obj in self.drawing.values():
            
            obj, rect = obj.get_drawinfo()
            screen_.blit(obj, rect)
    
    
    def draw(self, key):
        self.drawing[key].drawSelf()
        
        
    def action(self):
        pass
        
        
    def __repr__(self) -> str:        
        return "Drawing dict: " + str(self.drawing)

