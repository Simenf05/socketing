import pygame
pygame.init()

import game
# import socket_files
from consts import *

SIZE = 600

screenobj = game.window.Window((SIZE, SIZE))




mapdict = {
    "map0" : {
        "drawing" : {},
        "collition" : [],
        "actionList" : []
    },
    "map1" : {
        "drawing" : {},
        "collition" : [],
        "actionList" : []
    }
}




subdrawing = {}
subcollition = []
subActionList = []


for row_i, row in enumerate(MAP[0]):
    for col_i, col in enumerate(row):
        
        if col == " ":
            mapdict["map0"]["drawing"].update({f"col_i{col_i} row_i{row_i}" + str(row_i) : game.layout.blocks.empty.Empty(TILESIZE * col_i, TILESIZE * row_i, "/bilder/empty.png")})
            
        if col == "o":
            mapdict["map0"]["drawing"].update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.wall.Wall(TILESIZE * col_i, TILESIZE * row_i, "/bilder/wall.png")})
            mapdict["map0"]["collition"].append(mapdict["map0"]["drawing"][f"col_i{col_i} row_i{row_i}"].get_collition())
        
        if col == "a":
            mapdict["map0"]["drawing"].update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.action.nextScreenBlck.NextScreenBlck(TILESIZE * col_i, TILESIZE * row_i, "/bilder/action.png", screenobj, MAPSNAME[0], (100, 100))})
            mapdict["map0"]["actionList"].append(mapdict["map0"]["drawing"][f"col_i{col_i} row_i{row_i}"])

for row_i, row in enumerate(MAP[1]):
        for col_i, col in enumerate(row):
            
            if col == " ":
                mapdict["map1"]["drawing"].update({f"col_i{col_i} row_i{row_i}" + str(row_i) : game.layout.blocks.empty.Empty(TILESIZE * col_i, TILESIZE * row_i, "/bilder/empty.png")})
                
            if col == "o":
                mapdict["map1"]["drawing"].update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.wall.Wall(TILESIZE * col_i, TILESIZE * row_i, "/bilder/wall.png")})
                mapdict["map1"]["collition"].append(mapdict["map1"]["drawing"][f"col_i{col_i} row_i{row_i}"].get_collition())
            
            if col == "a":
                mapdict["map1"]["drawing"].update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.action.nextScreenBlck.NextScreenBlck(TILESIZE * col_i, TILESIZE * row_i, "/bilder/action.png", screenobj, MAPSNAME[1], (100, 100))})
                mapdict["map1"]["actionList"].append(mapdict["map1"]["drawing"][f"col_i{col_i} row_i{row_i}"])


mapLayout = game.layout.layout.Layout((1, 1))
button = game.layout.button.nextScreenBtn.NextScreen(10, 10, 50, 30, screenobj, "start", text="ESC", activeButton=pygame.K_ESCAPE)
mapLayout.setValue(button, (1, 1))

player = game.layout.blocks.players.player.Player(100, 200, "/bilder/player.png")

mapdict["map1"]["drawing"].update({"button" : button})
mapdict["map1"]["drawing"].update({"player" : player})
mapdict["map0"]["drawing"].update({"button" : button})
mapdict["map0"]["drawing"].update({"player" : player})



main = game.map.Map(player, mapdict["map0"]["drawing"], mapLayout, mapdict["map0"]["collition"], mapdict["map0"]["actionList"])
sub = game.map.Map(player, mapdict["map1"]["drawing"], mapLayout, mapdict["map1"]["collition"], mapdict["map1"]["actionList"])

newDraw = {}

for key, item in draw.items():
    match key.split("_")[0]:
        case "text":
            
            newDraw.update({
                key : game.layout.text.textBox.TextBox(item[0], item[1], item[2], item[3])
            })
        case "input":
            
            newDraw.update({
                key : game.layout.text.inputBox.InputBox(item[0], item[1], item[2], item[3], item[4])
            })
            
        case "button":
            
            item[4] = screenobj
            newDraw.update({
                key : game.layout.button.nextScreenBtn.NextScreen(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            })  

newLayout = {}

for key, item in settingLayout.items():
    newLayout.update({
        key : (newDraw[key], item)
    })

startLayout = game.layout.layout.Layout((5, 1))

for item in newLayout.values():
    startLayout.setValue(item[0], item[1])

start = game.menu.Menu(newDraw, startLayout)


screenobj.addScreen(("main", main))
screenobj.addScreen(("sub", sub))
screenobj.addScreen(("start", start), True)

run = True

# screenobj.addPlayerToAllMaps()

while run:
    
    pressed = pygame.key.get_pressed()

    screenobj.keypressReg(pressed)
    
    screenobj.updateScreen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    
