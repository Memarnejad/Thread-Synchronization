#be nam _e_ khoda
#Mehran Memarnejad 92521267
#Question number 3

import time
import threading

class device(threading.Thread):

    def __init__(self, resrc, semaphore):

        threading.Thread.__init__(self)
        self.resource = resrc
        self.free = 1
        self.semaphore = semaphore

    def run(self):

        self.semaphore.acquire()
        i = 0
        while i < len(self.resource) and self.resource[i][1] == 'Busy':
            i += 1
        self.resource[i][1] = 'Busy'
        self.free = i+1
        print "The resource %s acquired by %s\n" %(self.free, self.name)
        #Simulating using resource
        time.sleep(1)
        self.resource[i][1] = 'Free'
        print "The resource %s released by %s\n" %(self.free, self.name)
        self.semaphore.release()     


def main():

    #Number of resource instance
    insNum = 5
    #Simulating the resources and their status
    resource = []
    for i in range (0, insNum):
        resource.append([i+1, 'Free'])
    #maximum number of access is equal to the number of instance
    semaphore = threading.BoundedSemaphore(insNum)

    #Number of clients
    threadNum = 8

    threadList = []
    #Creating threads
    for i in range (0, threadNum):
        t = device(resource, semaphore)
        threadList.append(t)

    for thread in threadList:
        thread.start()

    for thread in threadList:
        thread.join()
        

if __name__ == '__main__':
    main()
 
