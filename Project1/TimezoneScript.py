from datetime import datetime
import pytz
#This imports the time stuff we will need to get times for each timezone.
userINList = input("Hello to the time script. If you know your timezone in Pytz form press N and hit enter. If not type 'list'. ")
rlist = 'list'
if userINList==rlist:
    for i in pytz.all_timezones:
        print(i)
#Everything above is about asking the user if they need to see what timezone they are and how it needs to be inputed into the input
userIN = input("Hello, what timezone are you from? Please enter in Pytz timezone form in the list above.")
rlist = 'list'
UIT = datetime.now(pytz.timezone(userIN))
#This is us asking the user what timezone and then storing it
print("The time in", (userIN), "is:", UIT.strftime("%Y:%m:%d %H:%M:%S %Z %z"))
#Here we output the time in the timezone the user stated

#ATTENTION
#If you run this in IDLE you need to install pytz so for easier use https://www.online-python.com/ to run the script without having to install module. 
