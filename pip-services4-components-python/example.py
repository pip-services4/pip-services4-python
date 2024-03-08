import threading
import time
import random


class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        print('Waiting for a lock')
        self.lock.acquire()
        try:
            print('Acquired a lock')
            self.value = self.value + 1
        finally:
            print('Released a lock')
            self.lock.release()


def worker(c):
    for i in range(2):
        r = random.random()
        print(f'Sleeping {r}')
        time.sleep(r)
        c.increment()
    print('Done')


if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()

    print('Waiting for worker threads')
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    print(f'Counter: {counter.value}')
