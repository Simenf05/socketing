import game.view as view
import time

class Map(view.View):
    """General class for maps to be shown on Window().

    Inherits from View.
    """
    def __init__(self, player: object, drawing: dict, layout: object, collition: list, actionList: list, mapName: str, onlinePlayer: dict={}, timediff: float =.16) -> None:
        """Sets up time variables and assigns lists.

        Args:
            player (object): Main Player() object to show. 
            drawing (dict): Dictionary containing everything to draw.
            layout (object): This will usually just be Layout() with escape button since arrow keys for navigation is disabled.
            collition (list): List containing all the blocks the player will collide with.
            actionList (list): List of all the blocks with actions connected.  
            onlinePlayer (dict, optional): Dictionary containing the other online players. Work in progress. Defaults to {}.
            timediff (float, optional): Time difference for actions. Defaults to .16.
        """
        
        super().__init__(drawing, layout)
        
        self.collition = collition
        self.actionList = actionList
        self.player = player
        
        self.mapName = mapName
        
        self.onlinePlayers = onlinePlayer
        
        self.nowTime = time.time()
        self.lastTime = {
            "up"    : self.nowTime,
            "down"  : self.nowTime,
            "left"  : self.nowTime,
            "right" : self.nowTime,
            "action": self.nowTime
            }
        
        self.timeDiff = timediff
    
        
    def addOPlayer(self, key: str, obj: object) -> None:
        """Adds online player.

        NOTE: Work in progress.
        
        Args:
            key (str): Key for the online player.
            obj (object): Object of the player block.
        """
        self.onlinePlayers.update({key : obj})
        
    def removePlayer(self, key: str) -> None:
        """Removes online player.

        NOTE: Work in progress.
        
        Args:
            key (str): Key of the player.
        """
        self.onlinePlayers.pop(key)
    
    def drawAll(self, screen_: object) -> None:
        """Draws all the components in the drawing dictionary.

        Args:
            screen_ (object): Main Window() object.
        """        
        
        for obj in self.drawing.values():
            
            obj, rect = obj.get_drawinfo()
            screen_.blit(obj, rect)
        
        for obj in self.onlinePlayers.values():
            obj, rect = obj.get_drawinfo()
            screen_.blit(obj, rect)
        
    
    def action(self, **kwargs) -> None:
        """Does the action and controls the player. Will be called every frame."""
        
        self.nowTime = time.time()
        
        kwargs.update({"actionLast": self.lastTime["action"]})
        kwargs.update({"nowTime"   : self.nowTime})
        kwargs.update({"timeDiff"  : self.timeDiff})
        
        self.layout.doAction(**kwargs)
        
        kwargs.update({"col" : self.collition})
        kwargs.update({"act" : self.actionList})
        kwargs.update({"mapName" : self.mapName})
        
        self.player.controls(**kwargs)
        
    
    