"""
I am pissed! I discovered the datetime.timedelta() function today.

This function can convert seconds to time (days, hours, min, seconds, and milliseconds).
Also, the function's max is something crazy like a million days.

My 90 line hack can be re-written and made better in ten lines of code.

This feeling sucks... 
"""

import os, time, datetime

def simple_way():
    
    infinite = "This is going to be used to create and infinite loop"
    
    while infinite == infinite:
                
        """
        This is the step by step explaination of my below variable.
        
        secs = str(time.clock())               Turn time.clock into a string
        secs = secs.split(".")                 Split to time.clock into seconds and milliseconds
        secs = secs[0]                         Select seconds
        secs = int(secs)                       Convert the seconds into an integer
        """
        
        secs = int(str(time.clock()).split(".")[0])
        
        timer = str(datetime.timedelta(seconds = secs)) #Use the datetime.timedelta() function to convert seconds to time
        os.system("cls")                                #clears screen
        print timer                                     #prints time to screen
        time.sleep(.1)                                  #Slows down the loop
        
        
simple_way()

if __name__ == '__main__':
    simple_way()
