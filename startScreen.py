from pygame import K_DOWN, K_ESCAPE, K_LEFT, K_UP
import screenFormat
import sys


class StartScreen(screenFormat.ScreenFormat):
    
    def __init__(self, drawing, layout) -> None:
        super().__init__(drawing, layout)
        
        
    def action(self, pressed):
        
        if pressed[K_UP]:
            self.layout.pos[0] -= 1
            
        if pressed[K_DOWN]:
            self.layout.pos[0] += 1
        
        if pressed[K_ESCAPE]:
            print(self.layout.pos)
            sys.exit()
            
        # legge til de andre knappene
            
        