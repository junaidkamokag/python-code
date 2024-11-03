# 20. Create a program that simulates a countdown timer starting from a given number down to zero.
import time
startTime= int(input("Enter Starting Time = "))
for i in range(startTime, -1 , -1):
    print (f"remaining time = {i}")
time.sleep(1)
print(f"time {startTime} seconds is over ")