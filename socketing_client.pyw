import socket
import random
import threading
import pygame
import json
import time
import logging

import layout
import textBox

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

color = "green"

pygame.init()

s = socket.socket()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

randomnr = random.randint(0, 500)

SCREENSIZE = 800
PLAYERSIZE = 40



class Game:

    
    def keydown(self, e):
        if e.key == pygame.K_a:
            self.activeMove["a"] = True
        elif e.key == pygame.K_w:
            self.activeMove["w"] = True
        elif e.key == pygame.K_s:
            self.activeMove["s"] = True 
        elif e.key == pygame.K_d:
            self.activeMove["d"] = True
    
    def keyup(self, e):
        if e.key == pygame.K_a:
            self.activeMove["a"] = False
        elif e.key == pygame.K_w:
            self.activeMove["w"] = False
        elif e.key == pygame.K_s:
            self.activeMove["s"] = False 
        elif e.key == pygame.K_d:
            self.activeMove["d"] = False

    
    def controls(self):

        

        while not self.crashed:

            for e in self.events:
                if e.type == pygame.KEYDOWN:
                    self.keydown(e)
                elif e.type == pygame.KEYUP:
                    self.keyup(e)
                    
                    
    def recving(self):

        while not self.crashed:
            try:
                self.data = s.recv(2048)
            
                self.usedData = json.loads(self.data.decode("utf-8"))
            except json.JSONDecodeError:
                continue
            except (ConnectionAbortedError, ConnectionResetError):
                return

    
    
    def sendEnd(self):
        s.send(
            json.dumps({
                        "info": "quit",
                        "sock": self.sock,
                        "box": None,
                        "color": None
                        }).encode("utf-8")
        )
        time.sleep(.005)
    
    
    def sendStart(self):
        s.send(
            json.dumps({
                        "info": "start",
                        "sock": self.sock,
                        "box": (self.box.x, self.box.y, self.box.w, self.box.h),
                        "color": color
                        }).encode("utf-8")
        )
        time.sleep(.005)


    def sending(self):

        self.sendStart()
        
        while not self.crashed:
            s.send(
                    json.dumps({
                        "info": "none",
                        "sock": self.sock,
                        "box": (self.box.x, self.box.y, self.box.w, self.box.h),
                        "color": color
                        }).encode("utf-8")
                )
            time.sleep(.005)
        
        
        

    def screenDraw(self, drawing: dict):
        pygame.draw.rect(self.screen, drawing["color"], drawing["box"])


    def running(self):

        self.controlThread.start()
        self.recvThread.start()
        self.sendThread.start()
        
        

        while not self.crashed:
            self.events = pygame.event.get()
            
            for e in self.events:
                if e.type == pygame.QUIT:
                    logging.debug("Recieved pygame.QUIT event")
                    
                    self.sendEnd()
                    
                    logging.debug("Siste data sendt")
                    
                    pygame.display.quit()
                    
                    logging.debug("Pygame display quit")
                    
                    pygame.quit()
                    
                    logging.debug("Pygame quit")
                    
                    self.crashed = True
                    
                    logging.debug("self.crashed flipped")
                    
                    return

            if self.activeMove["w"]:
                self.box.move_ip(0, -5)
            if self.activeMove["s"]:
                self.box.move_ip(0, 5)
            if self.activeMove["a"]:
                self.box.move_ip(-5, 0)
            if self.activeMove["d"]:
                self.box.move_ip(5, 0)
            

            self.screen.fill("black")

            if self.usedData:
                for key, d in self.usedData.items():
                    if key == self.sock:
                        continue
                    else:
                        self.screenDraw(d)

            pygame.draw.rect(self.screen, color, self.box)

            pygame.display.update()
            self.clock.tick(30)
        

    def startScreen(self):        
        
        overskrift = textBox.TextBox(int(SCREENSIZE / 2), int(SCREENSIZE / 6), "THE LEDGEND OF JON", self.GREEN, self.BIGFONT)
        pil = textBox.TextBox(int(SCREENSIZE / 2), int((SCREENSIZE / 5) * 1.5), "Bruk piltastene for å navigere", self.GREEN, self.NORMALFONT)
        brukernavn = textBox.TextBox(int(SCREENSIZE / 2), int((SCREENSIZE / 5) * 2), "Brukernavn", self.GREEN, self.NORMALFONT)
        
        ip = textBox.TextBox(int(SCREENSIZE / 2), int((SCREENSIZE / 5) * 3), "IP adresse", self.GREEN, self.NORMALFONT)
        
        skjerm = layout.Layout((1, 2))
        
        skjerm.setValue(overskrift, (1, 1))
        skjerm.setValue(ip, (1, 2))
        
        while self.onStartScreen:
            self.events = pygame.event.get()
            
            for e in self.events:
                if e.type == pygame.QUIT:
                    logging.debug("Recieved pygame.QUIT event")
                    
                    self.sendEnd()
                    
                    logging.debug("Last data sent")
                    
                    pygame.display.quit()
                    
                    logging.debug("Pygame display quit")
                    
                    pygame.quit()
                    
                    logging.debug("Pygame quit")
                    
                    self.crashed = True
                    self.onStartScreen = False
                    
                    logging.debug("self.crashed and self.onStartScreen flipped")
                    
                    return
            
            self.keys = pygame.key.get_pressed()
            
            for key in self.keys:
                if pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                    skjerm.keypress(key)
            
            self.screen.fill("black")
            
            
            self.screen.blit(overskrift.textObj, overskrift.textRect)
            self.screen.blit(brukernavn.textObj, brukernavn.textRect)
            self.screen.blit(pil.textObj, pil.textRect)
            self.screen.blit(ip.textObj, ip.textRect)
            
            pygame.display.update()
            self.clock.tick(30)

    
    def conn(self):
        s.connect((self.HOST, self.PORT))

        self.sock = s.recv(1024).decode("ascii")
        
    

    def __init__(self):

            self.activeMove = {
                "w": False,
                "s": False,
                "a": False,
                "d": False
            }

            self.pos = {
                "x": randomnr,
                "y": randomnr
            }

            
            self.controlThread = threading.Thread(target=self.controls)
            self.recvThread = threading.Thread(target=self.recving)
            self.sendThread = threading.Thread(target=self.sending)
            
            
            self.box = pygame.Rect(self.pos["x"], self.pos["y"], PLAYERSIZE, PLAYERSIZE)

            self.data = {}
            
            self.usedData = {}
            
            self.crashed = False
            self.onStartScreen = True

            self.events = pygame.event.get()
            self.screen = pygame.display.set_mode([SCREENSIZE, SCREENSIZE])
            self.clock = pygame.time.Clock()
            
            self.BIGFONT = pygame.font.Font(None, 52)
            self.NORMALFONT = pygame.font.Font(None, 42)
            self.SMALLFONT = pygame.font.Font(None, 32)
            
            self.RED = (255, 0, 0)
            self.GREEN = (0, 255, 0)
            self.BLUE = (0, 0, 255)
            
            self.HOST = socket.gethostname()
            self.PORT = 443
            
            
            
            
            
            


game = Game()
game.startScreen()

game.conn()

game.running()

time.sleep(1)

s.close()
