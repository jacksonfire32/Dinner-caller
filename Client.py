#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys
from socket import socket, AF_INET, SOCK_DGRAM
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
SERVER_IP   = '192.168.1.223'
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
a=1
while (a == 1):  
    if GPIO.input(11):
        print('Input was HIGH')
        mySocket = socket( AF_INET, SOCK_DGRAM )
        myMessage = "1"
        myMessage1 = ""
        mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        time.sleep(2)
    else:
        print('Input was LOW')
        mySocket = socket( AF_INET, SOCK_DGRAM )
        myMessage = "0"
        myMessage1 = ""
        mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        time.sleep(2)
