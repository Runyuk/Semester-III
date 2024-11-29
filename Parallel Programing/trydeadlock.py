import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    if lock1.acquire(timeout=1):
        print('thread 1: Lock 1 acuired, waiting for Lock 2...')
        if lock2.acquire(timeout=1):
            print('Trhead 1: Lock 2 Acuired')
            lock2.release()
        lock1.release()
def thread2():
    if lock2.acquire(timeout=1):
        print('thread 2: Lock 2 acuired, waiting for Lock 1...')
        if lock1.acquire(timeout=1):
            print('Trhead 2: Lock 1 Acuired')
            lock1.release()
        lock2.release()

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print('program selesai')