import pygame
import time
pygame.init()

import game
from consts import *

SIZE = 600

screenobj = game.window.Window((SIZE, SIZE))




drawing = {}
collition = []

for row_i, row in enumerate(MAP):
    for col_i, col in enumerate(row):
        
        if col == " ":
            drawing.update({f"col_i{col_i} row_i{row_i}" + str(row_i) : game.layout.blocks.empty.Empty(TILESIZE * col_i, TILESIZE * row_i, "/bilder/empty.png")})
            
        if col == "o":
            drawing.update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.wall.Wall(TILESIZE * col_i, TILESIZE * row_i, "/bilder/wall.png")})
            collition.append(drawing[f"col_i{col_i} row_i{row_i}"].get_collition())
            

mapLayout = game.layout.layout.Layout((1, 1))
button = game.layout.button.nextScreenBtn.NextScreen(10, 10, 90, 30, screenobj, "start", text="ENTER")
mapLayout.setValue(button, (1, 1))

player = game.layout.blocks.players.player.Player(400, 400, "/bilder/player.png")

drawing.update({"button" : button})
drawing.update({"player" : player})



main = game.map.Map(player ,drawing, mapLayout, collition)

drawing2 = {
    "button" : game.layout.button.nextScreenBtn.NextScreen(200, 200, 100, 20, screenobj, "main", "ENTER")
}

startLayout = game.layout.layout.Layout((1, 1))
startLayout.setValue(drawing2["button"], (1, 1))

start = game.menu.Menu(drawing2, startLayout)



screenobj.addScreen(("main", main))
screenobj.addScreen(("start", start), True)

run = True

screen = pygame.display.set_mode((SIZE, SIZE))

for i in collition:
    pygame.draw.rect(screen, "red", i)

pygame.display.update()

time.sleep(5)



while run:
    
    pressed = pygame.key.get_pressed()

    screenobj.keypressReg(pressed)
    
    screenobj.updateScreen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    
