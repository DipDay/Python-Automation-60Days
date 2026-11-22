import schedule
import time
from datetime import datetime

def task1():
    print("It's 10 seconds", datetime.now())

def task2():
    print("Current Time:", datetime.now())

def task3():
    print("Report Completed", datetime.now())


schedule.every(10).seconds.do(task1)
schedule.every(30).seconds.do(task2)
schedule.every(60).seconds.do(task3)

while True:
    schedule.run_pending()
    time.sleep(1)