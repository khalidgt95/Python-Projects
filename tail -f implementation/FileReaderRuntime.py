#!/usr/bin/python3

import time
import atexit

old_position = None

handle = open("dummy.txt",'r+')

def exitMethod():
    tempfile = open('saved.txt','w')
    tempfile.write(str(old_position))    

atexit.register(exitMethod)

try:
    savedHandle = open('saved.txt','r')
    index = int(savedHandle.readline().strip())
    
    handle.seek(index,0)
        
except FileNotFoundError:
    print('ok np')

while True:
    
    old_position = handle.tell()
 
    line = handle.readline()
    
    new_position = handle.tell()
    
    if line.strip() == '':
        handle.close()
        handle = open("dummy.txt",'r+')
        
        if handle.seek(0,2) < old_position - 1:
            old_position = handle.seek(0,2) 
            print(old_position)
            
        handle.seek(old_position,0)
        time.sleep(0.1)
        continue
    else:
        s = line + ' ' + str(old_position).strip()
        print(s)
    #new_position = handle.tell()    
    

