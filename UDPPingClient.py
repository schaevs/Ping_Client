'''
Created on Oct 15, 2016

@author: alexanderschaevitz
'''
import socket
import time
import datetime

PORT_SERVER = 6500
PORT_CLIENT = 12258 
HOST = "localhost"
data = "test"

socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.bind((HOST,PORT_CLIENT))
i=1



while (i <= 10):   
    cTime = time.ctime()
    data = time.strftime('%l:%M%p %Z on %b %d, %Y')
    try:
        socketClient.sendto(data, (HOST,PORT_SERVER))
        print i
        socketClient.settimeout(1)
        print socketClient.recv(1024)
    except:
        print ("request timed out")
    i = i + 1