'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-29
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-29
@Title : To get time eclipsed between stopwatch start and stop
/**********************************************************************************
'''
import time

def stopwatch():
    """
    Description:
        This function takes starting and stopping of stopwatch and calculates 
        time eclipsed between two using time module.     
    """
    try:
        # to start stopwatch
        start_value = int(input("enter 1 to start stopwatch: ")) # to start stopwatch
        if start_value == 1:
            # start timer using time.time()
            start = time.time()
            print("starting..........")
        
        stop_value = int(input("enter 0 to stop stopwatch: "))
        if stop_value == 0:
            print("ending........")
             # end time using time.time()
            end = time.time()
            # get time eclipsed
            print("elapsed time:  ", round((end - start), 2))
        else:
            raise ValueError
    # if user enters other than 1/0 then raise exception
    except ValueError:
        print("wrong value!! Please enter correct value")
        stopwatch()
    
stopwatch()