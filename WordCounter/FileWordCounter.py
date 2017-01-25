#!/usr/bin/python3

class database(object):
    
    dictionary = dict()
    
    def __init__(self,name):
        self.__name = name
        
    def insertWord(self,word):
        self.dictionary[word] = 1
        
    def searchWord(self,word):
        if word in self.dictionary:
            self.dictionary[word] += 1
        
        else:
            self.insertWord(word)  
            
    @staticmethod
    def getNameOfDictionary():
        print(self.__name)
    
    def printAllValues(self):
        for iterator in self.dictionary:
            print("Word: %s , Count: %d" % (iterator,self.dictionary[iterator]))

        
dbObject=database("Khalid's Dictionary")

fileObject = open("dummy.txt")

line = fileObject.readline()

while line:

    strObject = line.split( )
       
    for i in range(0,len(strObject)):
        dbObject.searchWord(str(strObject[i].lower()))
    
    line = fileObject.readline()        
        
dbObject.printAllValues()

