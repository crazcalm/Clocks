"""
This is my attempt at a digital clock!
"""

import os, time

def digital_clock():
    
    """
    I create an infinite loop. During this loop, I use both 
    time.localtime() and time.strftime(). The first function gives
    me the local time and the second function formats it.
    """
    
    infinite = "This is going ot be used to create an inifinte loop."
    
    while infinite == infinite:
        
        #%I = hours (1-12), %M = minutes, %S = seconds, %p = am or pm
        
        clock = time.strftime("%I:%M:%S %p", time.localtime())
        print clock
        time.sleep(0.5) # used to slow down the loop
        os.system("cls") # Clears the screen

if __name__ == '__main__':
    digital_clock()
