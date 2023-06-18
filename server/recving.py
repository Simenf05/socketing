import socket
import stoppableThread
import json
import __main__

from time import sleep

class Recving(stoppableThread.StoppableThread):
    """Class made for receiving data from the multiple clients.

    Is started by the Listen Thread.
    
    Inherits from StoppableThread.
    """
    
    def __init__(self, running: bool, s: socket.socket, sock: socket.socket, getData: dict, key: str, database: object, socketsSend: dict, nr: int) -> None:
        """Initializes the variables needed.

        Args:
            running (bool): Should be True.
            s (socket.socket): Main socket object. 
            sock (socket.socket): Socket object made for the connection. 
            getData (dict): Dictionary containing alle the players data.
            key (str): The key that this connection will manipulate. 
        """
        super().__init__()
        
        self.nr = nr
        
        self.s = s
        self.sock = sock
        self.getData = getData
        self.key = key
        self.database = database
        self.socketsSend = socketsSend
        
        self.running = running
    
    
    def run(self) -> None:
        """Method that will handle data sent from the connection."""
        
        new_player_info = self.sock[0].recv(1024).decode("utf-8")
        new_player_info = json.loads(new_player_info)
        
        name = new_player_info["name"]
        password = new_player_info["password"]
        color = new_player_info["color"]
        
        player_info = self.database.create_user(name, password, 100, 200, "map1", color)
        
        player_coords = self.database.getFromDB("coords", "*", f"coords_id={player_info[0][3]}")
        player_color = self.database.getFromDB("colr", "*", f"colr_id={player_info[0][4]}")
        
        senddata = {
            "id" : player_info[0][0],
            "name" : player_info[0][1],
            "password" : player_info[0][2],
            "x" : player_coords[0][1],
            "y" : player_coords[0][2],
            "map" : player_coords[0][3],
            "color" : player_color[0][1]
        }
        
        senddata = json.dumps(senddata)
        senddata = senddata.encode("utf-8")
        self.sock[0].send(senddata)
        
        sleep(.1)
        self.socketsSend.update({f"sock_{self.nr}" : self.sock})
        
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
                    
                    self.database.save_user(player_info[0][0], self.getData[self.key]["x"], self.getData[self.key]["y"], self.getData[self.key]["map"])
                
                self.getData.pop(self.key)
                self.sock[0].shutdown(socket.SHUT_RDWR)
                self.stop()
                continue
                
            
            self.getData.update({self.key : data})