import socket
import json
import logging

format = '%(levelname)-20s : %(asctime)-10s : %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

class Connection:
    
    def __init__(self, data, host: str, port: int) -> None:
        
        self.s = socket.socket()
        self.HOST = host
        self.PORT = port
        
        self.data = data
        
        self.logger = logging.Logger("clientLogger")
        self.logger.info(f"host is {self.HOST}")
        
        
        
    def disconnect(self):
        
        endData = json.dumps({
            "info" : "quit",
            "save" : True
        })
        
        self.s.send(endData.encode("utf-8"))
        
        self.s.close()
        
    
    
    def conn(self):
        
        self.s.connect((self.HOST, self.PORT))
        
        
        
    def recv(self):
        noe = self.s.recv(1024)
        print(noe)

    

logging.info("noe")

conn = Connection("10.2.1.190", 443)
    
conn.conn()    
conn.recv()