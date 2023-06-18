
import game.layout.blocks.blockFormat as blockFormat

# work in progress

class OnlinePlayer(blockFormat.BlockFormat):
    """Class for the players controlled by other people.

    Inherits from BlockFormat.
    """
    
    def __init__(self, x: int, y: int, path: str) -> None:
        """Needs baseclass arguments.

        Args:
            x (int): X position.
            y (int): Y position.
            path (str): Path to the image used for graphics.
        """
        super().__init__(x, y, path)
        