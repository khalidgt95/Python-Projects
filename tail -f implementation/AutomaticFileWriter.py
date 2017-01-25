#!/usr/bin/env python3

import time

handle = open('dummy.txt','a')

iterator = 1
while True:
    handle.write('Khalid Ahmed = %d\n' %(iterator))
    handle.flush()
    iterator += 1
    time.sleep(2)        

