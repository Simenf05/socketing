import socket
import threading
import logging
import time
import json




def writeNew(file, info):
    file.write(json.dumps(info))
    file.close()

def readNew(file):
    info = json.loads(file.read())
    file.close()
    return info


writeNew(open("info.json", "w"), {"heu": "hey"})

print(readNew(open("info.json")))



format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


# sockets = []

sockets = {}
threadDict = {}
getdata = {}

running = True

HOST = socket.gethostname()
PORT = 443

s = socket.socket()


def recvdata(s, addr):
    logging.info("motta starter")
    print(sockets, s)
    indexofshit = 0
    for succ in sockets:
        if succ[0] == s:
            break
        indexofshit += 1

    while running:
        try:
            print(getdata)

            getdata.update({})

            # getdata[indexofshit] = s.recv(1024)
            print(getdata[0].decode("ascii"))
        except ConnectionAbortedError and ConnectionResetError:
            sockets.pop(indexofshit)
            break
    logging.info("motta slutter")
    
    threadList.pop(indexofshit + 2)
    

def senddata(socketAndData):
    logging.info("send starter")
    # print(sockets)
    for sock in sockets:
        sock[0].send(str(socketAndData).encode("ascii"))
        
    logging.info("send slutter")


def game():
    while running:
        # print(time.time())
        # print(sockets)

        data = "hei"

        for sock in sockets:
            try:
                senddata((sock, data))
            except ConnectionAbortedError and ConnectionResetError:
                sockets.remove(sock)

        time.sleep(.5)
        

def conn():
    logging.info("kobling starter")
    s.bind((HOST, PORT))
    s.listen(5)
    nr = 1

    while running:
        
        sockets.update({"sock " + str(nr): s.accept()})
        threadDict.update({"thread " + str(nr + 2): threading.Thread(target=recvdata, args=(sockets["sock " + str(nr)]))})

        print(threadDict)
        print(sockets)


        threadDict["thread " + str(nr + 2)].start()
        nr += 1

    logging.info("kobling slutter")


threadDict.update({"thread conn": threading.Thread(target=conn)})
threadDict.update({"thread game": threading.Thread(target=game)})
threadDict["thread conn"].start()
threadDict["thread game"].start()
