
import socket
import time

import stoppableThread
import recving
import __main__


class Listen(stoppableThread.StoppableThread):
    
    def __init__(self, running, s: socket.socket, sockets, threads, host, port, getData) -> None:
        super().__init__()
        
        self.s = s
        self.sockets = sockets
        self.threads = threads
        self.getData = getData
        
        self.running = running
        
        self.s.bind((host, port))
        self.s.listen(5)
    
        
    def run(self) -> None:
        
        nr = 1
        
        while self.running:
            
            if self.stopped():
                break
            
            
            for key, thread in self.threads.copy().items():
                if thread.stopped():
                    self.threads.pop(key)
            
            try:
                self.sockets.update({f"sock_{nr}" : self.s.accept()})
            
            except TimeoutError:
                continue 
            
            except OSError:
                self.stop()
                break
                
            self.threads.update({f"thread_{nr}" : recving.Recving(self.s, self.sockets[f"sock_{nr}"], self.sockets[f"sock_{nr}"], self.getData, f"player_{nr}")})
            
            self.threads[f"thread_{nr}"].start()
            nr += 1
            
        
            