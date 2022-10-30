#The script works by entering a time in minutes as it is a short alarm clock and not a long one. I think as next step I will make a UI for the clock. 
#Another thing is I imported some stuff cause I wanted to add a UI for this at the start but I need to understand it more.

from distutils.cmd import Command
import time
from tkinter import *
import tkinter.messagebox
#This is me importing the time stuff we need and for future updates the tkinter UI stuff.


i = input("Enter time you need to count down from: ")
message = input("Enter a message you wish for the alarm to remind you with: ")
#These are my user input variables.
def timerclock(i):
    while i:
        mins, secs = divmod(i, 60)
        actualtimer = '{:02d}:{:02d}'.format(mins, secs)
        print(actualtimer, end="\r")
        time.sleep(1)
        i -= 1
        if i == 0:
            print(message)
#This is the actual program I only have it in minutes and seconds right now and will add hours and a UI in next version I think. 

timerclock(int(i))
#This calls the function I made essentially and runs the whole program.
