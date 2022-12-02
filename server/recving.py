import socket
import stoppableThread
import json
import __main__


class Recving(stoppableThread.StoppableThread):
    """Class made for receiving data from the multiple clients.

    Is started by the Listen Thread.
    
    Inherits from StoppableThread.
    """
    
    def __init__(self, running: bool, s: socket.socket, sock: socket.socket, getData: dict, key: str) -> None:
        """Initializes the variables needed.

        Args:
            running (bool): Should be True.
            s (socket.socket): Main socket object. 
            sock (socket.socket): Socket object made for the connection. 
            getData (dict): Dictionary containing alle the players data.
            key (str): The key that this connection will manipulate. 
        """
        super().__init__()
        
        # potensiell cleanup med self.s
        self.s = s
        self.sock = sock
        self.getData = getData
        self.key = key
        
        self.running = running
    
    
    def run(self) -> None:
        """Method that will handle data sent from the connection."""
        
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