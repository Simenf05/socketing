import socket
import threading
import logging
import time


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


sockets = []
threadList = []
getdata = [0]

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
            getdata[indexofshit] = s.recv(1024)
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

    while running:
        sockets.append(s.accept())

        threadList.append(threading.Thread(target=recvdata, args=(sockets[-1])))

        print(threadList)
        print(sockets)

        threadList[-1].start()

    logging.info("kobling slutter")


threadList.append(threading.Thread(target=conn))
threadList.append(threading.Thread(target=game))
threadList[0].start()
threadList[1].start()
