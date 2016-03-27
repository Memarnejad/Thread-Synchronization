#be nam _e_ khoda
#Mehran Memarnejad 92521267
#Question number 1

import threading
import sqlite3

class FetchInfos(threading.Thread):
    """
    Thread checking Students.
    """

    def __init__(self, info, dbName, lock):
        """
        Constructor.

        @param info list of students to write
        @param output file to write info output
        """
        threading.Thread.__init__(self)
        self.info = info
        self.db = dbName
        self.lock = lock
    
    def run(self):
        """
        Thread run method. Check students one by one.
        """
        conn = sqlite3.connect(self.db)
        
        while self.info:
            record = self.info.pop()
            self.lock.acquire()
            print 'lock acquired by %s' % self.name
            conn.execute(record)
            conn.commit()
            print 'A new record Added to Database by %s' % self.name
            print 'lock released by %s' % self.name
            self.lock.release()
        

def main():

    db = 'test.db'
    conn = sqlite3.connect(db)
    print "Opened database successfully";
    
    conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       SALARY         REAL);''')
    
    print "Table created successfully";
    conn.close()
    
    lock = threading.Lock()

    info1 = ["INSERT INTO COMPANY (ID,NAME,SALARY) \
      VALUES (1, 'Mohammad', 200.00 )", "INSERT INTO COMPANY (ID,NAME,SALARY) \
      VALUES (2, 'Ali', 150.00 )"]
    
    info2 = ["INSERT INTO COMPANY (ID,NAME,SALARY) \
      VALUES (3, 'Reza', 460.00 )", "INSERT INTO COMPANY (ID,NAME,SALARY) \
      VALUES (4, 'Hossein', 720.00 )"]
    
    t1 = FetchInfos(info1, db, lock)
    t2 = FetchInfos(info2, db, lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print "DataBase Closed Successfully"
    conn.close()

if __name__ == '__main__':
    main()
 
