import socket
import json

import stoppableThread

class Send(stoppableThread.StoppableThread):
    
    def __init__(self, s, running, playerData) -> None:
        super(Send, self).__init__()
        
        self.s = s
        self.running = running
        self.playerData = playerData
    
    def run(self):
        
        while self.running:
            if self.stopped():
                break
            
            sendData = self.playerData
            
            jsonData = json.dumps(sendData)
            
            try:
                self.s.send(jsonData.encode("utf-8"))
                
            except (ConnectionAbortedError, ConnectionResetError):
                self.stop()
                
            except OSError:
                self.stop()
                break