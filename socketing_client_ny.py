import socket
import random
import threading
import pygame
import pickle

HOST = socket.gethostname()
PORT = 443

s = socket.socket()

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
            self.data = pickle.loads(s.recv(1024))


    def sending(self):

        while not self.crashed:
            s.send(
                    pickle.dumps({
                        "box": self.box,
                        "color": "blue"
                        })
                )


    def screenDraw(self, drawing: dict):
        pygame.draw.rect(self.screen, drawing["color"], drawing["box"])


    def running(self):

        controlThread = threading.Thread(target=self.controls)
        recvThread = threading.Thread(target=self.recving)
        sendThread = threading.Thread(target=self.sending)

        controlThread.start()
        recvThread.start()
        sendThread.start()

        while not self.crashed:
            self.events = pygame.event.get()
            for e in self.events:
                if e.type == pygame.QUIT:
                    self.crashed = True

            if self.activeMove["w"]:
                self.box.move_ip(0, -5)
            if self.activeMove["s"]:
                self.box.move_ip(0, 5)
            if self.activeMove["a"]:
                self.box.move_ip(-5, 0)
            if self.activeMove["d"]:
                self.box.move_ip(5, 0)
            

            pygame.Surface.fill(self.screen, "black")

            if self.data:
                for key, d in self.data.items():
                    if key == self.sock:
                        continue
                    else:
                        self.screenDraw(d)

            pygame.draw.rect(self.screen, "blue", self.box)

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

            self.box = pygame.Rect(self.pos["x"], self.pos["y"], 20, 20)

            self.data = {}
            self.crashed = False

            self.events = pygame.event.get()
            self.screen = pygame.display.set_mode([500, 500])
            self.clock = pygame.time.Clock()
            
            s.connect((HOST, PORT))

            self.sock = s.recv(1024).decode("ascii")
            self.running()
            

game = Game()
