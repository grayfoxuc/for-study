import time
import os
clear = lambda: os.system('cls')

def countdown(time_sec, look_away):
    clear()
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Activity: {timeformat}", end='\r')
        time.sleep(1)
        time_sec -= 1
    clear()

    while look_away:
        mins, secs = divmod(look_away, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Look away: {timeformat}", end='\r')
        time.sleep(1)
        look_away -= 1
    clear()

def start_eyecare():
    try:
        activity = int(input("Enter activity time(seconds): "))
    except:
        activity = 1200
    try:
        look_away = int(input("Enter look away(seconds): "))
    except:
        look_away = 20

    while True:
        countdown(activity, look_away)
    clear()

start_eyecare()