

import socket
import json

host = socket.gethostbyname(socket.gethostname())

data = {
    "info" : print("hey")
    }

data2 = json.dumps(data)

with socket.socket() as s:
    s.connect((host, 443))
    s.send(data2.encode("utf-8"))
    print(s.recv(1024))