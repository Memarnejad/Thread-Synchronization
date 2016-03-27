#be nam _e_ khoda
#Mehran Memarnejad 92521267
#Question number 2

import threading

class FetchInfos(threading.Thread):
    """
    Thread checking Students.
    """

    def __init__(self, info, output, lock):
        """
        Constructor.

        @param info list of students to write
        @param output file to write info output
        """
        threading.Thread.__init__(self)
        self.info = info
        self.output = output
        self.lock = lock
    
    def run(self):
        """
        Thread run method. Check students one by one.
        """
        while self.info:
            student = self.info.pop()
            
            self.lock.acquire()
            print 'lock acquired by %s' % self.name
            self.output.write(student)
            print 'write done by %s' % self.name
            print 'lock released by %s' % self.name
            student = student.split()
            student = str(student[0]) + ' ' +str(student[1])
            print 'Student %s fetched by %s' % (student, self.name)
            self.lock.release()

def main():
    # list 1 of students to fetch
    info1 = ['Mehran Memarnejad \t 92521267\n', 'Sina Salehpour \t 90471183\n']
    # list 2 of students to fetch
    info2 = ['Mohammad Zolghadr \t 90431286\n', 'Reza Ebrahimi \t 89512054\n']
    lock = threading.Lock()
    f = open('output.txt', 'w+')
    t1 = FetchInfos(info1, f, lock)
    t2 = FetchInfos(info2, f, lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__ == '__main__':
    main()
 
