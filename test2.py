import pygame
pygame.init()

import game
# import socket_files
from consts import *

SIZE = 600

screenobj = game.window.Window((SIZE, SIZE))

mapdict = {}

for map_i in range(len(MAP)):
    mapdict.update({
        f"map_{MAPSNAME[map_i]}" : {
            "drawing" : {},
            "collition" : [],
            "actionList" : []
            }
    })

a_count = 0

for map_i, map in enumerate(MAP):
    for row_i, row in enumerate(map):
        for col_i, col in enumerate(row):
            if col == " ":
                mapdict[f"map_{MAPSNAME[map_i]}"]["drawing"].update({f"col_i{col_i} row_i{row_i}" + str(row_i) : game.layout.blocks.empty.Empty(TILESIZE * col_i, TILESIZE * row_i, "/bilder/empty.png")})
            
            if col == "o":
                mapdict[f"map_{MAPSNAME[map_i]}"]["drawing"].update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.wall.Wall(TILESIZE * col_i, TILESIZE * row_i, "/bilder/wall.png")})
                mapdict[f"map_{MAPSNAME[map_i]}"]["collition"].append(mapdict[f"map_{MAPSNAME[map_i]}"]["drawing"][f"col_i{col_i} row_i{row_i}"].get_collition())
        
            if col == "a":
                mapdict[f"map_{MAPSNAME[map_i]}"]["drawing"].update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.action.nextScreenBlck.NextScreenBlck(TILESIZE * col_i, TILESIZE * row_i, "/bilder/action.png", screenobj, ALINKS[a_count], (100, 100))})
                mapdict[f"map_{MAPSNAME[map_i]}"]["actionList"].append(mapdict[f"map_{MAPSNAME[map_i]}"]["drawing"][f"col_i{col_i} row_i{row_i}"])
                a_count += 1
            

mapLayout = game.layout.layout.Layout((1, 1))
button = game.layout.button.nextScreenBtn.NextScreen(10, 10, 50, 30, screenobj, "start", text="ESC", activeButton=pygame.K_ESCAPE)
mapLayout.setValue(button, (1, 1))
player = game.layout.blocks.players.player.Player(100, 200, "/bilder/player.png")

for map in mapdict.values():
    map["drawing"].update({"escapeButton" : button})
    map["drawing"].update({"player" : player})

maps = {}


for name in MAPSNAME:
    print(type(mapdict[f"map_{name}"]["actionList"][0]))
    maps.update({
        
        f"map_{name}" : game.map.Map(player, mapdict[f"map_{name}"]["drawing"], mapLayout, mapdict[f"map_{name}"]["collition"], mapdict[f"map_{name}"]["actionList"])
    })

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

for name in MAPSNAME:
    screenobj.addScreen((name, maps[f"map_{name}"]))
    
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
    
