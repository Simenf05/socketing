import pygame
pygame.init()

from pygame import K_RIGHT, K_UP, K_LEFT, K_DOWN
import game.layout.blocks.blockFormat as blockFormat

class Player(blockFormat.BlockFormat):
    """Main player class that can be controlled when playing.

    Inherits from BlockFormat.
    """
    def __init__(self, x: int, y: int, map: str, path: str, speed: int = 5) -> None:
        """Sets up bool vars and assigns speed.

        Args:
            x (int): X position.
            y (int): Y position.
            path (str): Path to the image used for graphics.
            speed (int, optional): The speed the player will move at. Defaults to 5.
        """
        super().__init__(x, y, path)

        self.speed = speed
        self.map = map
    
        self.hittingWall = {
            "top" : False,
            "bottom" : False,
            "left" : False,
            "right" : False,
            "topleft" : False,
            "topright" : False,
            "downleft" : False,
            "downright" : False
        }
        
        self.moveRect = pygame.rect.Rect(self.coords[0], self.coords[1], self.size[0], self.size[1])
    
    def reset(self, x, y, map, path):
        
        self.coords = [x, y]
        self.map = map
        self.set_path(path)
        
        pass
    
    def controls(self, **kwargs) -> None:
        """Moves the player. 
        
        Gets kwargs['col'] and kwargs['pressed'] from Map().
        """
        
        self.map = kwargs["mapName"]
        
        for direction in self.hittingWall:
            
            
            self.moveRect.x = self.coords[0]
            self.moveRect.y = self.coords[1]
            
            if direction == "top":
                self.moveRect.move_ip(0, -self.speed)
            elif direction == "bottom":
                self.moveRect.move_ip(0, self.speed)
                
            elif direction == "left":
                self.moveRect.move_ip(-self.speed, 0)
            elif direction == "right":
                self.moveRect.move_ip(self.speed, 0)
                
            elif direction == "topleft":
                self.moveRect.move_ip(-self.speed, -self.speed)
            elif direction == "topright":
                self.moveRect.move_ip(self.speed, -self.speed)
                
            elif direction == "downleft":
                self.moveRect.move_ip(-self.speed, self.speed)
            elif direction == "downright":
                self.moveRect.move_ip(self.speed, self.speed)
            
            for wall in kwargs["col"]:
                if pygame.Rect.colliderect(self.moveRect, wall):
                    self.hittingWall[direction] = True
            
            for act in kwargs["act"]:
                if pygame.Rect.colliderect(self.moveRect, act):
                    self.hittingWall[direction] = True
                    act.action(**kwargs)
        
        
        if (kwargs["pressed"][K_UP] and kwargs["pressed"][K_LEFT]):
            if not self.hittingWall["topleft"]:
                self.coords[0] -= self.speed
                self.coords[1] -= self.speed
            
            elif not self.hittingWall["top"]:
                self.coords[1] -= self.speed
            
            elif not self.hittingWall["left"]:
                self.coords[0] -= self.speed
            
        elif (kwargs["pressed"][K_UP] and kwargs["pressed"][K_RIGHT]):
            if not self.hittingWall["topright"]:
                self.coords[0] += self.speed
                self.coords[1] -= self.speed
            
            elif not self.hittingWall["top"]:
                self.coords[1] -= self.speed
                
            elif not self.hittingWall["right"]:
                self.coords[0] += self.speed
            
        elif (kwargs["pressed"][K_DOWN] and kwargs["pressed"][K_LEFT]):
            if not self.hittingWall["downleft"]:
                self.coords[0] -= self.speed
                self.coords[1] += self.speed
            
            elif not self.hittingWall["bottom"]:
                self.coords[1] += self.speed
                
            elif not self.hittingWall["left"]:
                self.coords[0] -= self.speed
                        
        elif (kwargs["pressed"][K_DOWN] and kwargs["pressed"][K_RIGHT]):
            if not self.hittingWall["downright"]:
                self.coords[0] += self.speed
                self.coords[1] += self.speed
                
            elif not self.hittingWall["bottom"]:
                self.coords[1] += self.speed
                
            elif not self.hittingWall["right"]:
                self.coords[0] += self.speed
            
        else:
        
            if kwargs["pressed"][K_UP] and not self.hittingWall["top"]:
                self.coords[1] -= self.speed
            
            if kwargs["pressed"][K_DOWN] and not self.hittingWall["bottom"]:
                self.coords[1] += self.speed
            
            if kwargs["pressed"][K_LEFT] and not self.hittingWall["left"]:
                self.coords[0] -= self.speed
                
            if kwargs["pressed"][K_RIGHT] and not self.hittingWall["right"]:
                self.coords[0] += self.speed
        
        for direction in self.hittingWall:
            self.hittingWall.update({direction : False})
        
        self.refresh()