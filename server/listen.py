import socket

import stoppableThread
import recving
# import __main__


class Listen(stoppableThread.StoppableThread):
    """Class made for listening for clients and acceping connections.

    Is started by the Server Thread and will start offspring-threads of Recving().
    
    Inherits from StoppableThread.
    """
    
    def __init__(self, running: bool, s: socket.socket, sockets: dict, threads: dict, host: str, port: int, getData: dict) -> None:
        """Binds the socket to the specified host and port, enables the server to accept connection by listening for 5 connections. 

        Args:
            running (bool): Should be True.
            s (socket.socket): Main socket object that will be bound and accepted on.
            sockets (dict): Dictionary containing all the socket connections.
            threads (dict): Dictionray containing all the running Threads. 
            host (str): The host to bind to.
            port (int): The port to bind to.
            getData (dict): The data that will be sent and changed by the connections.
        """
        super().__init__()
        
        self.s = s
        self.sockets = sockets
        self.threads = threads
        self.getData = getData
        
        self.running = running
        
        self.s.bind((host, port))
        self.s.listen(5)
    
        
    def run(self) -> None:
        """Method that will accept connections and start Recving() threads."""
        
        nr = 1
        
        while self.running:
            
            if self.stopped():
                break
            
            
            for key, thread in self.threads.copy().items():
                if thread.stopped():
                    self.threads.pop(key)
            
            try:
                self.sockets.update({f"sock_{nr}" : self.s.accept()})
                self.sockets[f"sock_{nr}"][0].send(f"sock_{nr}")
            
            except TimeoutError:
                continue 
            
            except OSError:
                self.stop()
                break
                
            self.threads.update({f"thread_{nr}" : recving.Recving(self.s, self.sockets[f"sock_{nr}"], self.sockets[f"sock_{nr}"], self.getData, f"player_{nr}")})
            
            self.threads[f"thread_{nr}"].start()
            nr += 1
            
        
            