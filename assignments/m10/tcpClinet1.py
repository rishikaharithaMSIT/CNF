import socket
import threading

def recvData(s):
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    name = input("ENTER NAME: ")
    s.send(name.encode())

    threading.Thread(target=recvData, args=(s,)).start()

    while True:
        message = input()
        s.send((name + ": " +message).encode())
    #data = s.recv(1024)
    #print(data.decode())
    #message = input("Name : ")
    #s.send(message.encode())
    # data = s.recv(1024)
    # print("Received from Server: " + str(data.decode()))

if __name__ == "__main__":
    main()