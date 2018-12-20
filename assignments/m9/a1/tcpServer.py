import socket
from random import randint
import threading

def th(s):
    c,addr = s.accept()
    print("Connection from : " + str(addr))
    ranNum = randint(0,50)
    print("RandNum: " + str(ranNum))
    guesses = 0
    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = int(data)
        guesses = guesses + 1
        sendData = "Nothing"
        if(data == ranNum):
            sendData = "correct, the guesses are: " + str(guesses)
            c.send(str(sendData).encode())
            c.close()
            return
        if(data < ranNum) :
            sendData = "Your number is less than guess"
        if(data > ranNum) :
            sendData = "Your number is greater than guess"
        c.send(str(sendData).encode())

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)

    t = list()
    for i in range(0,3):
        # s.listen(3)        
        t1 = threading.Thread(target=th, args=(s,))
        t.append(t1)
        t[i].start()
        # t[i].join()

    for i in range(0,3):
        t[i].join()
    # t2 = threading.Thread(target=th, args=(s,))
        
    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()

    print("DONE")

    #c.close()

if __name__ == "__main__":
    main()
    
