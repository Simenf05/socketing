import socket
import threading
import logging
import time
import pickle



format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


sockets = {}
threadDict = {}
getdata = {}

running = True

HOST = socket.gethostname()
PORT = 443

s = socket.socket()


def recvdata(sock, key):
    global getdata
    logging.info("motta starter")

    while running:
        try:
            getdata.update({key: pickle.loads(sock[0].recv(1024))})

        except (ConnectionAbortedError, ConnectionResetError, pickle.UnpicklingError, EOFError):
            sockets.pop(key)
            break
    logging.info("motta slutter")
    
    getdata.pop(key)
    threadDict.pop("thread " + str(int(key.split()[1]) + 2))
    

def senddata(socketAndData):
    for key, sock in sockets.items():
        try:
            sock[0].send(pickle.dumps(socketAndData[1]))
        except (ConnectionAbortedError, ConnectionResetError):
            sockets.pop(key)


def game():
    while running:

        data = getdata

        for key, sock in sockets.items():
            try:
                senddata((sock, data))
            except (ConnectionAbortedError, ConnectionResetError):
                sockets.pop(key)

        time.sleep(.0005)
        

def conn():
    logging.info("kobling starter")
    s.bind((HOST, PORT))
    s.listen(5)
    nr = 1

    while running:
        
        sockets.update({"sock " + str(nr): s.accept()})
        sockets["sock " + str(nr)][0].send(("sock " + str(nr)).encode("ascii"))

        threadDict.update({"thread " + str(nr + 2): threading.Thread(target=recvdata, args=(sockets["sock " + str(nr)], "sock " + str(nr)))})

        print(threadDict)
        print(sockets)

        threadDict["thread " + str(nr + 2)].start()
        nr += 1

    logging.info("kobling slutter")


threadDict.update({"thread conn": threading.Thread(target=conn)})
threadDict.update({"thread game": threading.Thread(target=game)})
threadDict["thread conn"].start()
threadDict["thread game"].start()
