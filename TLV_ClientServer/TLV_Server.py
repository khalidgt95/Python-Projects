#!/usr/bin/python3

from socket import *
import time
import multiprocessing  
import atexit
          

class server(object):
    
    __socket = None
    __echoQueue = dict()
    __messageQueue = dict()
    __alertQueue = dict()
    __databaseForSize = dict()
    __clientDatabase = dict()    
        
    def __init__(self):
        atexit.register(self.exitMethod)
            
    def typeQueueLogger(self,msgType,address):
        if address == 'ECHO':
            if address in self.__echoQueue:
                self.__echoQueue[address] += 1
            else:
                self.__echoQueue[address] = 1
            return
            
        elif address == 'MSG':
            if address in self.__echoQueue:
                self.__messageQueue[address] += 1
            else:
                self.__messageQueue[address] = 1
            return
            
        elif address == 'ALERT':
            if address in self.__echoQueue:
                self.__alertQueue[address] += 1
            else:
                self.__alertQueue[address] = 1
            return
    
    def databaseSizeLogger(self,lenOfMsg,address):
        if address in self.__databaseForSize:
            self.__databaseForSize[address] += lenOfMsg
        else:
            self.__databaseForSize[address] = lenOfMsg
                
                    
    def clientDatabaseLogger(self,value,address):
        priority = None
        
        if value['Priority'] == 'URGENT':
            priority = 'priority-urgent'
        if value['Priority'] == 'NORMAL':
            priority = 'priority-normal'
        
        timestamp = value['Timestamp']
        
        seqno = int(value['Seqno'])
        
        
        if address in self.__clientDatabase:
            
            self.__clientDatabase[address][priority] += 1
            self.__clientDatabase[address]['last-timestamp'] = timestamp
            self.__clientDatabase[address]['Seqno'] = seqno
            
        else:
            self.__clientDatabase[address] = {'priority-normal' : 0, 'priority-urgent' : 0, 'last-timestamp' : None, 'Seqno' : 0}
            self.__clientDatabase[address][priority] += 1
            self.__clientDatabase[address]['last-timestamp'] = timestamp
            self.__clientDatabase[address]['Seqno'] = seqno
            
            
    def clientSizeLogger(self,size,address):
        if address in self.__databaseForSize:
            self.__databaseForSize[address] += size 
        else:
            self.__databaseForSize[address] = size
         
           
    def parseMessage(self,message,address):
        
        typeOfMessage = message['Type']
        bytesOfMessage = message['Bytes']
        valueOfMessageDict = message['Value']
        
        self.typeQueueLogger(typeOfMessage,address)
        self.clientSizeLogger(bytesOfMessage,address)
        self.clientDatabaseLogger(valueOfMessageDict,address)
             
    def initializeServerAndStartTalking(self,port):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__socket.bind(('localhost',port))
        self.__socket.listen()
        
        client,addr = self.__socket.accept()
       
        print('Got a connection from %s' % ( str(addr) ))
        
        clientAddr = str(addr)
        
        while True:         
            bytesReceived = client.recv(4096)
            
            messageDict = eval(bytesReceived.decode())
            
            self.parseMessage(messageDict,clientAddr)
            
            self.printClientDataUsage()
            
            self.printClientDatabase()
            
    def exitMethod(self):
        print('\n\nSocket Closed !')
        
        try:
            self.__socket.close()
        except Exception:
            print('Something Happened')
        
    
    def printClientDatabase(self):
        print(self.__clientDatabase)
        
    def printClientDataUsage(self):
        print(self.__databaseForSize)
################################################################
                    # Main Starts here
################################################################

svObject = server()

svObject.initializeServerAndStartTalking(6004)
            
