'''
Created on Jun 28, 2016

@author: Neonkitza
'''
import threading
import time
from characters.Neonpewpew import Neonpewpew

exitFlag = 0
charNeonpewpew = Neonpewpew()
class MainThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        while True:
            self.counter+=1
            print(self.counter)
            

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1    

# Create new threads
thread1 = MainThread(1, "Thread-1", 1)
thread2 = MainThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")