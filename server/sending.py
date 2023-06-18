import json
import time

import stoppableThread
import __main__


class Send(stoppableThread.StoppableThread):
    """Class made for sending data to multiple clients.

    Is started by the Server Thread.
    
    Inherits from StoppableThread.
    """
    
    def __init__(self, running: bool, sockets: dict, getData: dict) -> None:
        """Initializes where to send to and what to send. 

        Args:
            running (bool): This should be True. 
            sockets (dict): Dictionary containing all the connections to send to.
            getData (dict): All the data to send, this will be manipulated by other threads. 
        """
        super(Send, self).__init__()
        
        self.sockets = sockets
        self.getData = getData
        self.running = running
    
    def run(self) -> None:
        """Method that will send the data out to all the clients."""
        
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
            