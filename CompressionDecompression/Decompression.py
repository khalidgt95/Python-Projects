#!/usr/bin/python3

class decompress(object):
    
    dictionary = dict()
    __count = 1
    original_list = list()    
    word = dict()
        
    def __init__(self):
        pass
        
    def decompressor(self):
        handle = open('output.txt')

        line = handle.readline()

        while line:
            temp = line.split(' {')
            key = temp[0]
           
            self.dictionary[key] = eval("{"+ temp[1])
            line = handle.readline()                               
        
        for keys,value in self.dictionary.items():              # value is the whole value pair
            for values in self.dictionary[keys]:                
                
                if values in self.word:
                    dummy = self.dictionary[keys][values]
                    for i in dummy:
                        mapstr = str(i)+":"+keys
                        self.word[values].insert(i,mapstr)
                else:
                    self.word[values] = list() 
                    dummy = self.dictionary[keys][values]
                    for i in dummy:
                        mapstr = str(i)+":"+keys
                        self.word[values].insert(i,mapstr)
                
            
    def printToFile(self):
    
        handle = open('decrypted.txt','w')
       
        for keys,value in self.word.items():
            '''tempdict = list()
            
            for iterator in value:
                temp = iterator.split(':')
                tempdict.append(temp[0])
            
            totalElements = max(tempdict)'''
            print(keys,value)            
        
            
deObject = decompress()

deObject.decompressor()
        
deObject.printToFile()        

