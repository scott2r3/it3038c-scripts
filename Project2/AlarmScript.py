#The script works by entering a time in minutes as it is a short alarm clock and not a long one. I think as next step I will make a UI for the clock. 
#Another thing is I imported some stuff cause I wanted to add a UI for this at the start but I need to understand it more.

from distutils.cmd import Command
import time
from tkinter import *
import tkinter.messagebox


i = input("Enter time you need to count down from: ")
message = input("Enter a message you wish for the alarm to remind you with: ")
def countclock(i):
    while i:
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        i -= 1
        if i == 0:
            print(message)



countclock(int(i))
