from fileinput import filename
from http import client
import socket
import threading
import os



def getFile(fileName,client):
    fileName = fileName.replace('Get','') # remove Get in file name
    fileName = fileName.replace(' ','') # remove whitespaces
    try:
        file = open(fileName,'rb')
        while True:
            context = file.read(1024)
            if not context:
                file.close()
                break
            client.send(context)
        client.close() 
    except:
         client.send("There is not such a file available!".encode())
         



def sendFile(fileName,client):
    fileName = fileName.replace('Put','') 
    fileName = fileName.replace(' ','')
    while True:
        mes = client.recv(1024) 
        if mes.decode()=="There is not such a file available!":
            print("No such a file!")
            break
        else:
            file = open(fileName,'wb')
            if not mes:
                print('file transformed!')
                file.close()
                break
            file.write(mes) 


def allFiles(client):
    #save file names indevidualy(not as an array) in a file
    list = os.listdir()
    ls = open('ls.txt','wt')
    for file in list:
        ls.write(file+'\n')
    ls.close()
    #send file info for client
    ls = open('ls.txt','rb')
    while True:
        data = ls.read(1024)
        if not data:
            break
        client.send(data)
    ls.close()
    #remove the ls file
    os.remove('ls.txt')
    client.close()



def handle(client,addr):
    print(str(addr)+" has connected to the server!")
    while True:
        fileName = client.recv(1024).decode()
        if 'Get' in fileName:
            getFile(fileName,client)
            break
        elif 'Put' in fileName:
            sendFile(fileName,client)
            break
        elif 'ls' in fileName:
            allFiles(client)
            break

            

def start():
    print("Server is running...")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('192.168.1.7',6000))
    while True:
        s.listen()
        client , addr = s.accept()
        t1 = threading.Thread(target=handle,args=(client,addr))
        t1.start()

if __name__ == "__main__":
    start()

     





 


 

