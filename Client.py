#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys
from socket import socket, AF_INET, SOCK_DGRAM
import time
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now
SERVER_IP   = '192.168.1.223'
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
a=1
while (a == 1):  
    if GPIO.input(11) == GPIO.HIGH:
        print("Button was pushed!")
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
