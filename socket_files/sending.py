import json
from . import stoppableThread
class Send(stoppableThread.StoppableThread):
    """Class made to send data to the server.

    Inherits from StoppableThread.
    """
    
    def __init__(self, s, running: bool, game: object) -> None:
        """Setup for sending with s.

        Args:
            s (socket.socket): The socket object to send with.
            running (bool): Should be True.
            playerData (dict): Data that will be sent, this can be changed while the thread is running.
        """
        
        super().__init__()
        
        self.s = s
        self.running = running
        self.game = game
    
    def run(self) -> None:
        """Method that will be called when Send.start() is called."""
        
        info = {
            "name" : self.game.mainwindow.screenDict["start"].drawing["input_name"].getText(),
            "password" : self.game.mainwindow.screenDict["start"].drawing["input_password"].getText(),
            "color" : self.game.mainwindow.screenDict["start"].drawing["input_color"].getText()
        }
        
        json_info = json.dumps(info)
        
        self.s.send(json_info.encode("utf-8"))
        
        startData = self.s.recv(2048).decode("utf-8")
        
        
        startData = json.loads(startData)
        
        self.game.create_player(startData["id"], startData["x"], startData["y"], startData["map"], startData["color"].split(".")[0])
        
        while self.running:
            if self.stopped():
                break
            
            
            sendData = {
                "x" : self.game.player.coords[0],
                "y" : self.game.player.coords[1],
                "map" : self.game.player.map,
                "info" : self.game.infodata,
                "color" : self.game.color
            }            
            jsonData = json.dumps(sendData)
            
            try:
                self.s.send(jsonData.encode("utf-8"))
                
            except (ConnectionAbortedError, ConnectionResetError):
                self.stop()
                
            except OSError:
                self.stop()
                break