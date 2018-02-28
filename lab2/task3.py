from threading import *
import random

my_lock = Lock()
fillCount = Semaphore(value = 0)
emptyCount = Semaphore(value = 10)

buffer = []

class ProducerThread(Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(0, 100)
            emptyCount.acquire()
            my_lock.acquire()
            buffer.append(item)
            my_lock.release()
            fillCount.release()


class ConsumerThread(Thread):
    def run(self):
        global buffer
        while True:
            fillCount.acquire()
            my_lock.acquire()
            item = buffer.pop();
            my_lock.release()
            emptyCount.release()
            print item

ProducerThread().start()
ConsumerThread().start()