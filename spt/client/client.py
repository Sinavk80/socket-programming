import os
import socket





def getFile(fileName):
    fileName = fileName.replace('Get','') # remove Get in file name
    fileName = fileName.replace(' ','') # remove whitespaces
    while True:
        mes = s.recv(1024)
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
     



def sendFile(fileName):
    fileName = fileName.replace('Put','') # remove Get in file name
    fileName = fileName.replace(' ','') # remove whitespaces
    try:
        file = open(fileName,'rb')
        while True:
            context = file.read(1024)
            if not context:
                print("file transformed!")
                file.close()
                break
            s.send(context)
        s.close()
    except:
         s.send("There is not such a file available!".encode()) #mes is for the server to now that file is not available
         print("There is not such a file available!")


def allFiles():
        while True:
            data = s.recv(1024)
            if not data:
                break
            print(data.decode())
        





while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '192.168.1.7'
    port = 6000
    s.connect((host,port))
    fileName = input('Enter the instruction:')
    s.send(fileName.encode())
    if 'Get' in fileName:
        getFile(fileName)
    elif 'Put' in fileName:
        sendFile(fileName)
    elif 'ls' in fileName:
        allFiles()
    elif 'Exit' in fileName:
        break
    else:
        print(fileName.split()[0]+" is not regognized as an instruction!")


        

