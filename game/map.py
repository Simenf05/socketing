import game.view as view


class Map(view.View):
    def __init__(self, player, drawing: dict, layout, collition) -> None:
        super().__init__(drawing, layout)
        
        self.collition = collition
        self.player = player
        
    def action(self, **kwargs): 
        
        kwargs.update({"col" : self.collition})
        
        self.player.controls(**kwargs)
        
    
    