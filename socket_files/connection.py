import socket
import json
import logging

format = '%(levelname)-20s : %(asctime)-10s : %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

class Connection:
    """Object used to connecting to the server."""
    
    def __init__(self, data, host: str, port: int) -> None:
        """_summary_

        Args:
            data (any): Data that will be sent and cheanged on recving
            host (str): The host to connect to
            port (int): The port to connect on
        """
        
        self.s = socket.socket()
        self.HOST = host
        self.PORT = port
        
        self.data = data
        
        self.logger = logging.Logger("clientLogger")
        self.logger.info(f"host is {self.HOST}")
        
        
        
    def disconnect(self):
        """Disconnect form the server"""
        
        endData = json.dumps({
            "info" : "quit",
            "save" : True
        })
        
        self.s.send(endData.encode("utf-8"))
        
        self.s.close()
        
    
    
    def conn(self):
        """Connect to the server"""
        
        self.s.connect((self.HOST, self.PORT))
        
        
        
    def recv(self):
        """work in progress"""
        noe = self.s.recv(1024)
        print(noe)

