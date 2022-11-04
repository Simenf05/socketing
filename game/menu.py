from pygame import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP
import game.view as view
import time
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")


class Menu(view.View):
    
    def __init__(self, drawing, layout, timediff: float =.16) -> None:
        super().__init__(drawing, layout)
        
        self.nowTime = time.time()
        self.lastTime = {
            "up": self.nowTime,
            "down": self.nowTime,
            "left": self.nowTime,
            "right": self.nowTime,
            "action": self.nowTime
            }
        
        self.timeDiff = timediff
        
        
    def action(self, **kwargs):
        self.nowTime = time.time()
        
        kwargs.update({"actionLast": self.lastTime["action"]})
        kwargs.update({"nowTime": self.nowTime})
        kwargs.update({"timeDiff": self.timeDiff})
        
        self.layout.doAction(**kwargs)
        
        internalPos = self.layout.getPos()
        
        if kwargs["pressed"][K_UP] and internalPos[0] > 1 and (self.nowTime - self.lastTime["up"] > self.timeDiff):
            internalPos[0] -= 1
            self.lastTime["up"] = self.nowTime
            
            
        if kwargs["pressed"][K_DOWN] and internalPos[0] < self.layout.dim[0] and (self.nowTime - self.lastTime["down"] > self.timeDiff):
            internalPos[0] += 1
            self.lastTime["down"] = self.nowTime
            
            
        if kwargs["pressed"][K_LEFT] and internalPos[1] > 1 and (self.nowTime - self.lastTime["left"] > self.timeDiff):
            internalPos[1] -= 1
            self.lastTime["left"] = self.nowTime
            
        
        if kwargs["pressed"][K_RIGHT] and internalPos[1] < self.layout.dim[1] and (self.nowTime - self.lastTime["right"] > self.timeDiff):
            internalPos[1] += 1
            self.lastTime["right"] = self.nowTime              
        
        if not internalPos[0] == self.layout.getPos()[0] or not internalPos[1] == self.layout.getPos()[1]:
            self.layout.updatePos(internalPos)
        
        """
        if kwargs["pressed"][K_ESCAPE]:
            if screen.onScreen == "main":
                screen.setOnScreen("start")
            else:
                screen.setOnScreen("main")
            
        """
            
        