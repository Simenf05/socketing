import pygame
pygame.init()
import game
import socket_files
from consts import *

import time

class Game:
    
    def __init__(self, screenSize: int) -> None:
        
        self.mainwindow = game.window.Window((screenSize, screenSize))
        self.player = game.layout.blocks.players.player.Player(100, 200, "map1", "bilder/red.png")
        
        self.port = 8069
        
        self.infodata = "new"
        self.color = "red"
        self.id = ...
        
        self.onlineData = {}
        self.onlinePlayers = {}
        
        self.connection = socket_files.connection.Connection(self)
        
        self.maps = self.create_maps()
        self.startView = self.create_start()
        
        for name in MAPSNAME:
            self.mainwindow.addScreen((name, self.maps[f"map_{name}"]))
        
        self.mainwindow.addScreen(("start", self.startView), True)
    
    def create_maps(self) -> dict[game.map.Map]:
        
        def create_map_dict():
            mapdict = {}
            for map_i in range(len(MAP)):
                mapdict.update({
                    f"map_{MAPSNAME[map_i]}" : {
                        "drawing" : {},
                        "collition" : [],
                        "actionList" : []
                        }
                })
            return mapdict
        
        def create_map_objects(self, mapdict):
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
                            mapdict[f"map_{MAPSNAME[map_i]}"]["drawing"].update({f"col_i{col_i} row_i{row_i}" : game.layout.blocks.action.nextScreenBlck.NextScreenBlck(TILESIZE * col_i, TILESIZE * row_i, "/bilder/action.png", self.mainwindow, ALINKS[a_count], (100, 100))})
                            mapdict[f"map_{MAPSNAME[map_i]}"]["actionList"].append(mapdict[f"map_{MAPSNAME[map_i]}"]["drawing"][f"col_i{col_i} row_i{row_i}"])
                            a_count += 1

            return mapdict
            
        mapdict = create_map_dict()
        mapdict = create_map_objects(self, mapdict)
        
        mapLayout = game.layout.layout.Layout((1, 1))
        button = game.layout.button.nextScreenAndDelConnBtn.NextScreenAndDelConnBtn(10, 10, 50, 30, self, "start", text="ESC", activeButton=pygame.K_ESCAPE)
        mapLayout.setValue(button, (1, 1))
        
        for map in mapdict.values():
            map["drawing"].update({"escapeButton" : button})
            map["drawing"].update({"player" : self.player})

        maps = {}
        
        for name in MAPSNAME:
            maps.update({
                f"map_{name}" : game.map.Map(self.player, mapdict[f"map_{name}"]["drawing"], mapLayout, mapdict[f"map_{name}"]["collition"], mapdict[f"map_{name}"]["actionList"], name)
            })

        return maps
        
    def create_start(self) -> game.menu.Menu:
        
        def create_draw(self):
            startDraw = {}
            
            for key, item in DRAW.items():
                match key.split("_")[0]:
                    case "text":
                        startDraw.update({
                            key : game.layout.text.textBox.TextBox(item[0], item[1], item[2], item[3])
                        })
                    case "input":
                        startDraw.update({
                            key : game.layout.text.inputBox.InputBox(item[0], item[1], item[2], item[3], item[4])
                        })
                    case "button":
                        item[4] = self.mainwindow
                        startDraw.update({
                            key : game.layout.button.nextScreenBtn.NextScreen(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
                    })
                    case "connbutton":
                        item[4] = self
                        startDraw.update({
                            key : game.layout.button.nextScreenAndConnBtn.NextScreenAndConnBtn(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
                    })
            return startDraw
        
        def create_layout(startDraw):
            startLayoutDict = {}
            
            for key, item in SETTINGLAYOUT.items():
                startLayoutDict.update({
                    key : (startDraw[key], item)
                })
            
            startLayout = game.layout.layout.Layout(LAYOUT_DIMENTIONS)
            
            for item in startLayoutDict.values():
                startLayout.setValue(item[0], item[1])
            
            return startLayout
        
        draw = create_draw(self)
        layout = create_layout(draw)
        start = game.menu.Menu(draw, layout)
        return start
        
    def connect_to_server(self, host: str, port: int):
        
        self.connection.conn(host, port)
        
        self.infodata = "new"
        self.connection.startThreads()
        
    def disconnect_from_server(self):
        
        self.connection.disconnect()
        self.connection.stopThreads()
        self.connection.refresh_vars()
        
    def check_online_data(self):
        
        
        for key, item in self.onlineData.copy().items():
            # print(key)
            if key.split("_")[1] == self.connection.get_id():
                
                continue
            
            if item["info"] == "quit":
                self.onlinePlayers.pop(key)
            
            if item["info"] == "new":
                self.onlinePlayers.update({key : game.layout.blocks.players.onlinePlayer.OnlinePlayer(item["x"], item["y"], "/bilder/red.png")})
                self.mainwindow.addPlayerToAllMaps(key, self.onlinePlayers[key])
        
    def create_player(self, id: int, x: int, y: int, map: str, color: str):
        self.color = color
        self.id = id
        self.player.reset(x, y, map, f"/bilder/{color}.png")
            
        

if __name__ == "__main__":
    run = True
    final = Game(600)
    
    while run:
        
        pressed = pygame.key.get_pressed()
        
        final.mainwindow.keypressReg(pressed)
        
        final.check_online_data()
        
        final.mainwindow.updateScreen()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                if final.connection.id:
                    final.disconnect_from_server()
                    
                final.connection.s.close()
                pygame.quit()
                run = False
        
    
    
    
    
    
    

    