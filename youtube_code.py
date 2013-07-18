"""
This code is from http://www.youtube.com/watch?v=6n5vW3DhElw. 

Thank you for putting this online!
"""

import os, time

seconds = 0
minutes = 0
hours   = 0

while seconds <=60:
    
    os.system("cls")
    print hours, "Hours", minutes, "Minutes", seconds, "Seconds"
    time.sleep(1)
    seconds +=1
    
    if seconds == 60:
        
        minutes += 1
        seconds  = 0
        
    elif minutes ==60:
        
        hours  +=  1
        minutes = 0
        seconds = 0
