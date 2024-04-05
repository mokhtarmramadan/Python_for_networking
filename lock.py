''' Locks a resourse while being used by a thread '''
from threading import Thread, Lock
import time

x = 50

lock = Lock()

def double():
    ''' Mulitpies x by 2 till it's 100'''
    global x
    lock.acquire()
    while x < 100:
        x *= 2
        print(x)
        time.sleep(2)
    print("Reached the maximun")
    lock.release()


def half():
    ''' Divides x by two till x = 1'''
    global x
    lock.acquire()

    while x > 1:
        x /= 2
        print(x)
        time.sleep(2)
    lock.release()

t1 = Thread(target=double)
t2 = Thread(target=half)

t1.start()
t2.start()