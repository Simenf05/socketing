
import json
from . import stoppableThread

from time import sleep

class Recv(stoppableThread.StoppableThread):

    def __init__(self, s, running: bool, game: object) -> None:
        
        super().__init__()
        
        self.game = game
        
        self.s = s
        self.running = running
        self.id = None
        
    
    def addId(self, id: str):
        self.id = id.split("_")[1]
    
    
    def run(self):
        
        sleep(.1)
        
        while self.running:
            if self.stopped():
                break
            
            try:
                onlineData = self.s.recv(1024).decode("utf-8")
                onlineData = json.loads(onlineData)
                self.game.onlineData = onlineData
                
                
            except json.JSONDecodeError:
                print("decode error")
                continue
            
            except (ConnectionAbortedError, ConnectionResetError):
                print("disconnected")
                self.stop()
                
            except OSError:
                print("osError")
                self.stop()
                break