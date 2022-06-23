import math
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
                progressBar(0,len(numbers)) #progress = 0 and totla=len(numbers)
                for i,x in enumerate(numbers):
                    results.append(math.factorial(x)) #append fact(x) to result list
                    progressBar(i+1,len(numbers)) #updating the bar
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
                progressBar(0,len(numbers))
                for i,x in enumerate(numbers):
                    results.append(math.factorial(x))
                    progressBar(i+1,len(numbers))
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
    
#progress bar function
def progressBar(progress,total):
    percent = 100 * (progress/float(total)) #percentage of charachters
    bar = '#' * int(percent)+ '-'*(100-int(percent))
    print(f"\r|{bar}|{percent:.2f}%",end='\r')

numbers = [x for x in range(4000,5000)]
results = []





while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '192.168.1.8'
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


        

