import time
import socket
import json
import threading
import logging

import listen
import sending

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

class Server:
    
    def __init__(self, HOST: str, PORT: int) -> None:
        
        self.HOST = HOST
        self.PORT = PORT
        
        self.s = socket.socket()
        
        self.s.settimeout(.1)
        
        self.sockets = {}
        self.threads = {}
        self.getData = {}
        
        self.running = True
        
        self.listening = listen.Listen(self.running ,self.s, self.sockets, self.threads, self.HOST, self.PORT, self.getData)
        self.sending = sending.Send(self.running, self.sockets, self.getData)
        
    def run(self):
        
        self.listening.start()
        self.sending.start()
        
    def close(self):
        
        self.listening.stop()
        self.listening.join()
        
        self.sending.stop()
        self.sending.join()
        
        # print(self.threads)
        
        for thread in self.threads.values():
            
            thread.stop()
            thread.join()
            
        self.s.close()
        

ip = socket.gethostbyname(socket.gethostname())
port = 443


print(f"Server on ip: {ip} and port: {port}")

server = Server(ip, port)

server.run()

while True:
    if input("write 'quit' to stop the server: ") == "quit":
        if input("sure y / n: ") in ["y", "Y"]:
            break
        
server.close()

