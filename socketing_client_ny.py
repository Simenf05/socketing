import socket
import threading
import pygame
import time

HOST = "192.168.0.191"
PORT = 443

with socket.socket() as s:
    s.connect((HOST, PORT))

    for i in range(10):
        s.send("100, 100".encode("ascii"))
        time.sleep(1)
    # data = s.recv(1024)
    # print(data.decode("ascii"))

"""heihei"""