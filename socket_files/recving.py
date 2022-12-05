
import json
from . import stoppableThread
class Recv(stoppableThread.StoppableThread):

    def __init__(self, s, running: bool, onlineData: dict) -> None:
        
        super().__init__()
        
        self.onlineData = onlineData
        
        self.s = s
        self.running = running
        self.id = None
        
    
    def addId(self, id: str):
        self.id = id.split("_")[1]
    
    def run(self):
        while self.running:
            if self.stopped():
                break
            
            try:
                onlineData = self.s.recv(1024).decode("utf-8")
                onlineData = json.loads(onlineData)
                self.onlineData = onlineData
                
            except json.JSONDecodeError:
                continue
            
            except (ConnectionAbortedError, ConnectionResetError):
                self.stop()
                
            except OSError:
                self.stop()
                break