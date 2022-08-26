import socket
import random
import threading
import pygame
import time

HOST = socket.gethostname()
PORT = 443

s = socket.socket()

randomnr = random.randint(1, 10)



class game:

    
    

    def controls(self):
        pass


    def screenDraw(self, drawing: dict):


        pass


    def running(self):

        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    self.crashed = True



            pass


    def __init__(self):
            pygame.init()

            self.crashed = False
            self.screen = pygame.display.set_mode([500, 500])

            s.connect((HOST, PORT))



with socket.socket() as s:
    s.connect((HOST, PORT))

    for i in range(4):
        s.send("100, 100".encode("ascii"))
        time.sleep(1)
    # data = s.recv(1024)
    # print(data.decode("ascii"))

