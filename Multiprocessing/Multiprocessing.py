import os
import time
from multiprocessing import Process, current_process
def square(numbers):
    for i in range(numbers):
        time.sleep(0.5)
        result= i*i
        processID= current_process().name
        print(f"The number {i} squares to {result}:  {processID}")
        


if __name__ == "__main__":
    processes=[]
    numbers= range(100)
    for number in range(50):
        process= Process(target=square, args=(number,))
        processes.append(process)

        # Processes are spawned by creating a Process object and 
        # then calling its start() method
        process.start()
    for process in processes:
        process.join()

    print("Multiprocessing complete")