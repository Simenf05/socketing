import json
from . import stoppableThread
class Send(stoppableThread.StoppableThread):
    """Class made to send data to the server.

    Inherits from StoppableThread.
    """
    
    def __init__(self, s, running: bool, playerData: dict) -> None:
        """Setup for sending with s.

        Args:
            s (socket.socket): The socket object to send with.
            running (bool): Should be True.
            playerData (dict): Data that will be sent, this can be changed while the thread is running.
        """
        
        super().__init__()
        
        self.s = s
        self.running = running
        self.playerData = playerData
    
    def run(self) -> None:
        """Method that will be called when Send.start() is called."""
        
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