import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c,addr = s.accept()
    print("Connection from : " + str(addr))

    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = str(data)
        con = data.upper()
        print("Sending data: " + str(con))
        c.send(str(con).encode())
    c.close()

if __name__ == "__main__":
    main()
