import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print('thread 1 : mengunci lock1')
        threading.Event().wait(1)
    with lock2:
        print('thread 1: mengunci lock2')
def thread2():
    with lock2:
        print('thread 2 : mengunci lock2')
        threading.Event().wait(1)
    with lock2:
        print('thread 2: mengunci lock1')

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print('program selesai')