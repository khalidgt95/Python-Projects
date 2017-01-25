#!/usr/bin/python3

class compression(object):
    
    dictionary = dict()
    linenumber = 1
    
    def __init__(self):
        pass
                
    def checker(self,word):
        if word in self.dictionary:
            return True
        else:
            return False
        
    def compressor(self,word,position):
        hasWord = self.checker(word)
        
        if hasWord:
            if self.linenumber in self.dictionary[word]:
                self.dictionary[word][self.linenumber].append(position)
            else:
                self.dictionary[word].update({self.linenumber:[position]})
        else:
            self.dictionary[word] = {self.linenumber : [position]}
    
    def valueReader(self,filename):
        fileObject = open(filename)
        
        line = fileObject.readline()
        
        while line:
            strObject = line.split()
            
            for i in range(0,len(strObject)):
                self.compressor(strObject[i],i)
                
            self.linenumber += 1
            line = fileObject.readline()
       
        fileObject.close()
             
    def printValues(self):
        for keys,values in self.dictionary.items():
            print(keys,values)
               
        return self.dictionary
        
    def printValuesToFile(self):
        fileObject = open("output.txt","w")
        
        for keys,values in self.dictionary.items():
            fileObject.write(str(keys)+" "+str(values)+"\n")
            
        fileObject.close()
            
            
################################################## 
#           Main Code Starts here
##################################################           
compObject = compression()

compObject.valueReader('dummy.txt')

returnValue = compObject.printValues()            
                            
compObject.printValuesToFile()             
