import socket
import logging

import listen
import sending
import database

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

class Server:
    """Main class for the server side scripts.
    
    This should recive and send data to the clients while shutting down closed connections and accepting new connections.
    """
    
    def __init__(self, HOST: str, PORT: int) -> None:
        """Initializes the server on set host address and port.

        Args:
            HOST (str): The host to serve from.
            PORT (int): The port to use.
        """
        
        self.HOST = HOST
        self.PORT = PORT
        
        self.s = socket.socket()
        
        self.s.settimeout(.1)
        
        self.sockets = {}
        self.socketsSend = {}
        self.threads = {}
        self.getData = {}
        
        self.running = True
        
        self.db = database.Database("localhost", "root", "", "game_info")
        
        self.listening = listen.Listen(self.running ,self.s, self.sockets, self.threads, self.HOST, self.PORT, self.getData, self.db, self.socketsSend)
        self.sending = sending.Send(self.running, self.socketsSend, self.getData)
        
    def run(self) -> None:
        """Starts the server."""
        
        self.listening.start()
        self.sending.start()
        
    def close(self) -> None:
        """Closes the server and the socket object."""
        
        self.listening.stop()
        self.listening.join()
        
        self.sending.stop()
        self.sending.join()
        
        for thread in self.threads.values():
            
            thread.stop()
            thread.join()
            
        self.s.close()
        

# Code that starts the server

if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    port = 8069


    print(f"Server on ip: {ip} and port: {port}")

    server = Server(ip, port)

    server.run()

    while True:
        if input("write 'quit' to stop the server: ") == "quit":
            if input("sure y / n: ") in ["y", "Y"]:
                break
            
    server.close()

