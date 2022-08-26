from re import T
import socket
import random
import threading
import pygame
import time

HOST = socket.gethostname()
PORT = 443

s = socket.socket()

randomnr = random.randint(0, 500)



class Game:

    
    def keydown(self, e):
        if e.key == pygame.K_a:
            self.activeMove.a = True
        elif e.key == pygame.K_w:
            self.activeMove.w = True
        elif e.key == pygame.K_s:
            self.activeMove.s = True 
        elif e.key == pygame.K_d:
            self.activeMove.d = True
    
    def keyup(self, e):
        if e.key == pygame.K_a:
            self.activeMove.a = False
        elif e.key == pygame.K_w:
            self.activeMove.w = False
        elif e.key == pygame.K_s:
            self.activeMove.s = False 
        elif e.key == pygame.K_d:
            self.activeMove.d = False

    
    def controls(self):

        while not self.crashed:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    print("keydown")
                    self.keydown(e)
                elif e.type == pygame.KEYUP:
                    self.keyup(e)
                    

        

    def recving(self):
        pass

    def sending(self):
        pass


    def screenDraw(self, drawing: dict):


        pass


    def running(self):



        controlThread = threading.Thread(target=self.controls)
        recvThread = threading.Thread(target=self.recving)
        sendThread = threading.Thread(target=self.sending)

        controlThread.start()

        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

            pygame.Surface.fill(self.screen, "black")
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
            self.screen = pygame.display.set_mode([500, 500])
            self.clock = pygame.time.Clock()
            self.running()

            
            # s.connect((HOST, PORT))
            


game = Game()


"""
with socket.socket() as s:
    s.connect((HOST, PORT))

    for i in range(4):
        s.send("100, 100".encode("ascii"))
        time.sleep(1)
    # data = s.recv(1024)
    # print(data.decode("ascii"))
"""
