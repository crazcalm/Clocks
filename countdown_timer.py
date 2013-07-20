"""
This is my countdown timer!  

:)


"""

import os, time, datetime

def user_input():
    
    """
    Collects the user input for start time.
    """
    
    user_input = raw_input("Please give me a starting time (ex HH:MM:SS): ")
    
    return user_input

def conversion(start_time):
    
    """
    Takes the user input, which is a string of "hours: minutes: seconds" 
    and converts it into seconds.
    """
    
    tempt = start_time.split(":")
    
    hours   = int(tempt[0])
    minutes = int(tempt[1])
    seconds = int(tempt[2])
    
    total_seconds = (hours * 60**2) + (minutes * 60) + seconds
    
    print "total seconds:", total_seconds
    
    return total_seconds

def countdown(time_left):
    
    """
    Takes the total seconds and converts it into time (mauch thanks to
    the datetime.timedelta function).
    
    In the while loop, I clear  the screen (os.system("cls")),
    I print the time to the screen, and then the loop
    sleeps for a second. Lastly, I subtract 1 from the total seconds
    (variable: time_left)
    """
    
    seconds_past = 0
    
    while time_left > 0:
        
        os.system("cls")
        print str(datetime.timedelta(seconds = time_left))
        time.sleep(1)
        
        time_left -=1
        
    return True 

def alarm(done):
    
    """
    This is the Alarm to notify you that the countdown is down.
    
    """
    
    if done == True:
        
        """
        Prints "Time is UP" to the screen and opens a song on my computer.
        """
        
        print "\n\nTime is UP!!!"
        os.startfile("C:\\Users\\RS011874\\Music\\downloaded music\\Thank You (Amended Album Version).mp3")  
        
        raw_input("Press enter to exit the progrom: ")
        
    else:
        pass
    
    
def main():
    
    """
    This function controls the flow of the program.
    """
    
    user = user_input()
    start_time = conversion(user)
    clock = countdown(start_time)
    finished = alarm(clock)
    

if __name__ == '__main__':
    main()
    
    
