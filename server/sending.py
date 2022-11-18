import json
import time

import stoppableThread
import __main__


class Send(stoppableThread.StoppableThread):
    
    def __init__(self, running, sockets, getData) -> None:
        super(Send, self).__init__()
        
        self.sockets = sockets
        self.getData = getData
        self.running = running
    
    def run(self) -> None:
        
        while self.running:
            
            if self.stopped():
                break
            
            sendData = self.getData
            
            jsonData = json.dumps(sendData)
            
            try:
                for key, socket in self.sockets.copy().items():
                    socket[0].send(jsonData.encode("utf-8"))
                
            except (ConnectionAbortedError, ConnectionResetError):
                self.sockets.pop(key)
                
            except OSError:
                self.stop()
                break
            
            time.sleep(.02)
            