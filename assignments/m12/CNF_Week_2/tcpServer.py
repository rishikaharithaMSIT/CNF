import socket
from random import randint
import threading
import csv

clientList = list()
rollnumbers = list()
questions = {}
answers = {}

def th(c):    
    while True:

        command = c.recv(1024)
        command = command.decode()

        li = command.split(" ")
        if(li[0] == "MARK-ATTENDANCE"):
            if li[1] in rollnumbers:
                while True:
                    message = "SECRETQUESTION: " + questions[li[1]]
                    c.send(message.encode())
                    answer = c.recv(1024)
                    answer = answer.decode()
                    ans  = answer.split(" ")
                    #print(answer + " - "+answers[li[1]])
                    if(ans[1] == answers[li[1]]):
                        message = "ATTENDANCE-SUCCESS"
                        c.send(message.encode())
                        break
                    else:
                        message = "ATTENDANCE-FAILURE"
                        c.send(message.encode())

            else :
                message = "ROLLNUMBER-NOTFOUND"
                c.send(message.encode())
        if not command:
            break
        #print("from connected user " +str(command)) 
        
        

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(3)

    with open('data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            rollnumbers.append(row[0])
            questions[row[0]] = row[1]
            answers[row[0]] = row[2]
    # print(questions)
    # print(answers)
    print("Valid Numbers are: ")
    for each in rollnumbers:
        print(each)
            


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
    
