
import threading

class StoppableThread(threading.Thread):
    
    
    def __init__(self) -> None:
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()
        
    def stop(self):
        self._stop_event.set()
        
    def stopped(self):
        return self._stop_event.is_set()