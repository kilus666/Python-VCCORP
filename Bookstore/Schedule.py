
import schedule
import time
import pandas as pd

def task1():
    print("Pokemon is great")

def task2():
    print("Please enter you name")
    Name= input(": ")
    print(f"you are the best {Name}!!!!")

schedule.every().day.at("11:17").do(task2)
while 1:
    schedule.run_pending()
    time.sleep(1)
