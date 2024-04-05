''' Printing hello and No in parallel using threads '''
import threading

def Hello():
    for i in range(1000):
        print("hello")

def No():
    for i in range(1000):
        print("No")

t1 = threading.Thread(target=Hello)
t2 = threading.Thread(target=No)
t1.start()
t2.start()