from pygame import K_RIGHT, K_UP, K_LEFT, K_DOWN
import game.layout.blocks.blockFormat as blockFormat

class Player(blockFormat.BlockFormat):
    def __init__(self, x: int, y: int, path: str, speed=6) -> None:
        super().__init__(x, y, path)

        self.speed = speed
    
    
    
    
    def controls(self, **kwargs):
        
        for rect in kwargs["col"]:
            if self.rect.colliderect(rect):
                print(rect)
        """
        if self.rect.collidelist(kwargs["col"]) == -1:
            print(kwargs["col"])
            return
        """
        
        if kwargs["pressed"][K_UP]:
            self.coords[1] -= self.speed
        
        if kwargs["pressed"][K_DOWN]:
            self.coords[1] += self.speed
        
        if kwargs["pressed"][K_LEFT]:
            self.coords[0] -= self.speed
            
        if kwargs["pressed"][K_RIGHT]:
            self.coords[0] += self.speed