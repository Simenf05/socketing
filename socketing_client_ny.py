import socket
import random
import threading
import pygame
import json
import time
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")


color = input("color: ")

HOST = "10.2.1.190"
PORT = 443

s = socket.socket()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

randomnr = random.randint(0, 500)



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
        


    def __init__(self):
            pygame.init()

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
            
            
            self.box = pygame.Rect(self.pos["x"], self.pos["y"], 20, 20)

            self.data = {}
            
            self.usedData = {}
            
            self.crashed = False

            self.events = pygame.event.get()
            self.screen = pygame.display.set_mode([500, 500])
            self.clock = pygame.time.Clock()
            
            s.connect((HOST, PORT))

            self.sock = s.recv(1024).decode("ascii")
            
            
            

game = Game()
game.running()

time.sleep(1)

logging.debug("Closing socket and quiting")

s.close()