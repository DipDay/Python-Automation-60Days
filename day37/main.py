import schedule
import time
from datetime import datetime

def task1():
    print("Task 1 Completed")
    return schedule.CancelJob

def task2():
    print("Task 2 Completed")
    return schedule.CancelJob

def task3():
    print("Task 3 Completed")
    return schedule.CancelJob

def task4():
    print("Current Time:", datetime.now())

schedule.every(5).seconds.do(task1)
schedule.every(10).seconds.do(task2)
schedule.every(15).seconds.do(task3)

# More
schedule.every().minute.do(task1)
schedule.every().hour.do(task2)
schedule.every().monday.do(task3)
schedule.every().day.at("22:30").do(task4)


# Schedule the job every day at 12:53 (PM)
schedule.every().day.at("12:53").do(task4)

while True:
    schedule.run_pending()

    if not schedule.jobs:
        break
    
    time.sleep(1)