import pygame
pygame.init()

import game.layout.blocks.blockFormat as blockFormat



class Empty(blockFormat.BlockFormat):
    """Class for the empty blocks that have no collition.

    Inherits from BlockFormat.
    """
    def __init__(self, x: int, y: int, path: str) -> None:
        """Needs the baseclasses arguments.

        Args:
            x (int): X position.
            y (int): Y position.
            path (str): Path to the image used for graphics.
        """
        super().__init__(x, y, path)
        
        
        
    