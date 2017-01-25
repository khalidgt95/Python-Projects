# Notifier example from tutorial
#
# See: http://github.com/seb-m/pyinotify/wiki/Tutorial
#
import pyinotify
import time


class EventHandler(pyinotify.ProcessEvent):
    
    def __init__(self,filename,fileHandle):
        self.__filename = filename
        self.__fileHandle = fileHandle
        
        self.__oldPosition = self.__fileHandle.tell()
        
    def process_IN_MODIFY(self, event):
        if '.swp' not in event.pathname:
        
            self.__oldPosition = self.__fileHandle.tell()
            line = self.__fileHandle.readline()
            
            if line.strip() != '':
                print(line)    
                    
def main(filename):
    
    handle = open(filename,'r')
    
    wm = pyinotify.WatchManager()  # Watch Manager
    wm.add_watch('/home/khalid/Documents/Python Practice/', pyinotify.ALL_EVENTS, rec=True)
    
    handler = EventHandler(filename,handle)
    notifier = pyinotify.Notifier(wm, handler)
   
    notifier.loop()
   
if __name__=='__main__':
    main('dummy.txt')
