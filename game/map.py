import game.view as view
import time

class Map(view.View):
    def __init__(self, player, drawing: dict, layout, collition, actionList, onlinePlayer: dict={}, timediff: float =.16) -> None:
        
        super().__init__(drawing, layout)
        
        self.collition = collition
        self.actionList = actionList
        self.player = player
        
        self.onlinePlayers = onlinePlayer
        
        self.nowTime = time.time()
        self.lastTime = {
            "up": self.nowTime,
            "down": self.nowTime,
            "left": self.nowTime,
            "right": self.nowTime,
            "action": self.nowTime
            }
        
        self.timeDiff = timediff
    
        
    def addOPlayer(self, key: str, obj):
        self.onlinePlayers.update({key : obj})
        
    def removePlayer(self, key: str):
        self.onlinePlayers.pop(key)
        
    def action(self, **kwargs): 
        
        self.nowTime = time.time()
        
        kwargs.update({"actionLast": self.lastTime["action"]})
        kwargs.update({"nowTime": self.nowTime})
        kwargs.update({"timeDiff": self.timeDiff})
        
        self.layout.doAction(**kwargs)
        
        kwargs.update({"col" : self.collition})
        kwargs.update({"act" : self.actionList})
        
        self.player.controls(**kwargs)
        
    
    