#!/usr/bin/python3

from socket import *
import time
import sys
import atexit

class generator(object):
   
    __seqno = 1
    __keywords = ['urgent','need','important','!','soon','quickly','help']
    __priority = 'NORMAL'
    
    __socketObject = None
    
    def __init__(self):
        self.__socketObject = socket(AF_INET,SOCK_STREAM)

        self.__socketObject.connect(('localhost',6004))
        
    def sendMessage(self,dictObject):
    
        self.__socketObject.send(str(dictObject).encode('ascii'))
        
        
    def userInteractFunction(self):
        while True:
            messageType = input('Enter type of message (ECHO,MSG,ALERT) : ')
            
            if messageType.strip().lower() not in ['echo','msg','alert']:            # If user gives wrong choice
                messageType = 'MSG'
                
            message = input('Enter your message (q to quit) : ')
                            
            if message == 'q':
                sys.exit()
                      
            timestamp = time.ctime(time.time()).split(' ')
            
            for iterator in self.__keywords:
                if iterator in message.lower():
                    self.__priority = 'URGENT'
                    break
            
            
            packet = {'Type': messageType.upper(),    
                      'Bytes' : len(message.encode('ascii')),  
                      'Value' : {'Timestamp' : timestamp[3], 'Priority' : self.__priority ,
                                 'Seqno' : self.__seqno },
                      'Message' : message }   
            
            self.__priority = 'NORMAL'          # Revert back to original value
            self.sendMessage(packet)
            
            print('\n################## Message Sent ####################\n')
            self.__seqno += 1

################################################################
                    # Main Starts here
################################################################
genObject = generator()

genObject.userInteractFunction()
