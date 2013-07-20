"""
This is my attempt at making a more accurate timer.
"""

import os, time



def format_time(time):
    
    """
    time is a list with hours, minutes, and seconds.
    
    This function checks to see if the item in this list
    is a double digit or a single digit. 
    
    If double digits, make it an int and display that number.
    
    if single digit, make it a string and add a "0" in front of it. 
    """
    
    for number in range(len(time)):
        
        try:
            time[number] = int(time[number][0:2])
            
        except:
            time[number] = "0" + time[number][0]
            
    return time


def parsing_time(clock):
    
    """
    Parses clock, which is currently a string version of the
    time.gmtime() output.
    """
    
    #Isolates hours, minutes, and seconds
    clock = clock.split(" ")    
    clock = [clock[3], clock[4], clock[5]]
    
    #Isolates the values of hours, minutes, and seconds
    for num in range(len(clock)): 
        
        tempt = clock[num].split("=")
        clock[num] = tempt[1]
    
    return clock



def main():
    
    """
    This function creates an infinite loop. During this loop,
    the timer will be printed to the screen, cleared from the
    screen, and then re-printed to the screen over and over again.
    """
    
    infinite = "This is going to be used to create an infinite loop..."
    
    while infinite == infinite:
        
        #Using time.gmtime() to convert time.clock() into
        #hours, minutes, and seconds
        #variable clock is a string so that I can parse it later
        
        clock = str(time.gmtime(time.clock()))
        
        #Parsing of clock
        #timer[hours, minutes, seconds]
        
        timer = parsing_time(clock)
        
        
        #Formating the hours, minutes, and seconds
        
        timer = format_time(timer)
        
        os.system("cls") # Clears the screen
        print "%s Hours %s Minutes %s Seconds" %(timer[0], timer[1], timer[2])
        time.sleep(0.2) #Used to slow down this process

if __name__ == '__main__':
    main()
