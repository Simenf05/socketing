import socket
import json
import logging

from . import sending
from . import recving

format = '%(levelname)-20s : %(asctime)-10s : %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

class Connection:
    """Object used to connecting to the server."""
    
    def __init__(self, game: object) -> None:
        """_summary_

        Args:
            data (any): Data that will be sent and cheanged on recving
            host (str): The host to connect to
            port (int): The port to connect on
        """
        
        self.s = socket.socket()
        self.host = None
        self.port = None
        self.id = None
        
        self.game = game
        
        self.send = sending.Send(self.s, True, self.game)
        self.recv = recving.Recv(self.s, True, self.game)
        
        self.logger = logging.Logger("clientLogger")
        self.logger.info(f"Host is {self.host}")
        
    def get_id(self):
        return self.id
    
    def refresh_vars(self):
        self.s = socket.socket()
        self.host = None
        self.port = None
        self.id = None
        
        self.send = sending.Send(self.s, True, self.game)
        self.recv = recving.Recv(self.s, True, self.game)
    
    def disconnect(self):
        """Disconnect form the server."""
        
        self.id = None
        
        endData = json.dumps({
            "info" : "quit",
            "save" : True
        })
        
        self.s.send(endData.encode("utf-8"))
        
    def conn(self, *args):
        """Connect to the server."""
        
        if len(args) >= 2:
            self.host, self.port = args[0], args[1]
        
        if not (self.host or self.port):
            raise TypeError("Host or port not defined.")
        
        self.s.connect((self.host, self.port))
        
        self.id = self.s.recv(1024).decode("utf-8")
    
    def startThreads(self):
        self.send.start()
        
        self.recv.addId(self.id)
        
        self.recv.start()
        
    def stopThreads(self):
        self.send.stop()
        self.recv.stop()
        
        
        
    """
    def recv(self):
        # work in progress
        noe = self.s.recv(1024)
        print(noe)"""