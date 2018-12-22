import socket
import threading

limit = 2

def recvData(s):
        while True:
            data = s.recv(1024)
            data = data.decode()
            if(data =="ATTENDANCE-FAILURE") :
                global limit
                print(data)
                if(limit == 0):
                    print("You are out of attemps!")
                    break
                else :
                    limit = limit - 1
                    print("You have " + str(limit+1) + " attemps more.")
            else :
                print(data)
   

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    # name = input("ENTER NAME: ")
    # s.send(name.encode())

    threading.Thread(target=recvData, args=(s,)).start()

    while True:
        message = input()
        s.send(message.encode())
    #data = s.recv(1024)
    #print(data.decode())
    #message = input("Name : ")
    #s.send(message.encode())
    # data = s.recv(1024)
    # print("Received from Server: " + str(data.decode()))

if __name__ == "__main__":
    main()