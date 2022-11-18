import socket
import stoppableThread
import json
import __main__

import time

class Recving(stoppableThread.StoppableThread):
    
    def __init__(self, running, s: socket.socket, sock, getData, key) -> None:
        super().__init__()
        
        self.s = s
        self.sock = sock
        self.getData = getData
        self.key = key
        
        self.running = running
    
    def quit(self):
        self.running = False
    
    def run(self):
        
        while self.running:
            
            if self.stopped():
                break
            
            try:
                data = self.sock[0].recv(2048)            
            except (ConnectionAbortedError, ConnectionResetError):
                self.stop()
                continue
            except OSError:
                self.stop()
                continue
            
            try:
                data = json.loads(data.decode("utf-8"))
            except json.JSONDecodeError:
                continue
            
            
            if data["info"] == "quit":
                
                if data["save"]:
                    
                    # lagre til database
                    
                    pass
                
                self.sock[0].shutdown(socket.SHUT_RDWR)
                self.stop()
                continue
                
            
            self.getData.update({self.key : data})