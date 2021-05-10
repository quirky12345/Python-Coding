#Thread is a light weighted process
#initially Hello and Hi will run on same thread "Main"
#we will make Hello and Hi class to take a different thread to run
#if we run them in parallel, there might be collision sometimes because our
# processor is too fast
# to run them alternately we will use sleep
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(8):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(8):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

# To run different threads at the same time we have to use start instead
# of run, and start will execute run() inside of it
t1.start()
# even if we are providing 1 sec sleep for both Hi and Hello, we can see
# collision again, it might be because when they are waking up
# they are take executing in same CPU
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")
# In total, there are three threads now: main thread, t1, and t2