#python code to illustrate 
#abs() built-in  function
# floating point number
from sqlite3 import Time
from time import time_ns


float = -53.26
print('Absolute value of float is:',abs(float))
# An integer
int =-94
print('Absolute value of intefer is:',abs(int))
# A complex number
complex = (3-4j)
print('Absolute value of a complex number is:',abs(complex))


# function to calculate speed
def cal_speed(dist,time):
    print("Distance(km):",dist)
    print("Timer(hr)",time)
    return dist/time
def cal_dis(speed,time):
    print("Time(hr):",time)
    print("Speed(km/hr):",speed)
    return speed*time
# Function to calculate time taken
def cal_time(dist,speed):
    print("Distance(km):",dist)
    print("speed(km/hr):",speed)
    return speed*dist

#calling function cal_speed()

print("calculated speed :",cal_speed(abs(45.9),abs(2.0)))
print(" ") 
# Calling function cal_dis()
print("The calculated Distance(km):",cal_dis(abs(63.9),abs(2.5)))
print("")
#calling function cal_time()
print("The calculated timer(hr):",cal_time(abs(48.0),abs(4.5)))
