
import threading

class StoppableThread(threading.Thread):
    """Derived class from the threading.Thread class
    
    This class should be subclassed to create stoppable threads. 
    """
    
    def __init__(self) -> None:
        """Initiates the threading inheritance."""
        super().__init__()
        self._stop_event = threading.Event()
        
    def stop(self):
        """Stops the thread."""
        self._stop_event.set()
        
    def stopped(self) -> bool:
        """Checks if the thread is stopped."""
        return self._stop_event.is_set()
    
