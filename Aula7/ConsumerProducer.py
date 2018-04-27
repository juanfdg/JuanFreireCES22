from threading import Thread, Lock
import time
import random

shared_item = 0
itens_done = 0
available = False

class Producer(Thread):
    global shared_item
    global available

    def __init__(self, lock):
        Thread.__init__(self)
        self.lock = lock
        self.produced = False

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.lock.acquire()
            if self.produced == False:
                shared_item = item
                self.produced = True
                available = True
                print('Producer notify: item Nº%d added by %s\n' % (item, self.name))
                time.sleep(1)
            self.lock.release()


class Consumer(Thread):
    global shared_item
    global itens_done
    global available

    def __init__(self, lock):
        Thread.__init__(self)
        self.lock = lock

    def run(self):
        global available
        while itens_done < 10:
            self.lock.acquire()
            if available:
                item = shared_item
                available = False
                print('Consumer notify: %d consumed by %s' % (item, self.name))
            self.lock.release()


if __name__ == '__main__':
    lock = Lock()
    t1 = Producer(lock)
    t2 = Consumer(lock)
    t3 = Consumer(lock)
    t4 = Consumer(lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()