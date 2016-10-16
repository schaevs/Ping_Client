'''
Created on Oct 15, 2016

@author: alexanderschaevitz
'''
# UDPPingServer.py
# We will need the following module to generate randomized lost packets
import random
import socket
# create a UDP socket
#notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('',6500))
while True:
    #Generate random number in the range of 0 to 10
    rand = random.randint(0,10)
    #Recieve the client packet along with the address it is comign from
    message, address = serverSocket.recvfrom(1024)
    #capitalize the message from the client
    message = message.upper()
    #If rand is less than 4, we consider the packet lost and do not respond
    if rand <4:
        continue
    #otherwise, the server responds
    serverSocket.sendto(message, address)