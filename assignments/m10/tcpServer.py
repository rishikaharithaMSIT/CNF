import socket
from random import randint
import threading

clientList = list()

def broadcast(message, client):
    #print(name + ": ")
    print(len(clientList))
    for c in clientList:
        #print("//////")
        if(c != client):
            c.send(message.encode())

def th(client):
    
    name = client.recv(1024)
    name = name.decode()

    broadcast(name + " has joined chat!", client)
    
    while True:
        data = client.recv(1024)
        data = data.decode()
        if not data:
            break
        print("from connected user " +str(data)) 
        broadcast(data, client)
        

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(3)

    # t = list()
    for i in range(0,3):
        # s.listen(3) 
        c,addr = s.accept()
        clientList.append(c)

        print("Connection from : " + str(addr))
        #clientList[i].send(("Enter your name and join the chat: ").encode())

        threading.Thread(target=th, args=(clientList[i],)).start()
    # for i in range(0,2):       
    #     t1 = threading.Thread(target=th, args=(clientList[i],i))
    #     t.append(t1)
    #     t[i].start()
    #     # t[i].join()

    
    # t2 = threading.Thread(target=th, args=(s,))
        
    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()

    print("DONE")

    #c.close()

if __name__ == "__main__":
    main()
    
