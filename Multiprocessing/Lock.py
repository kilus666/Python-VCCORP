import time
import logging
from multiprocessing import Process, Lock, Value
from multiprocessing import log_to_stderr, get_logger

def add500Lock(total):
    for i in range(100):
        Lock().acquire()
        total.value+=5
        Lock().release()

def sub500Lock(total):
    for i in range(100):
        Lock().acquire()
        total.value-=5
        Lock().release()

if __name__=="__main__":
    total= Value("i", 500)
    addProcess= Process(target= add500Lock, args=(total,))
    subProcess= Process(target= sub500Lock, args=(total,))

    addProcess.start()
    subProcess.start()

    addProcess.join()
    subProcess.join()
    
    print("Done", total.value)


