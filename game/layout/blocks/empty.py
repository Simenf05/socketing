import pygame
pygame.init()

import game.layout.blocks.blockFormat as blockFormat



class Empty(blockFormat.BlockFormat):
    def __init__(self, x: int, y: int, path: str) -> None:
        super().__init__(x, y, path)
        
        
        
    