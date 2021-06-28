'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-28
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-28
@Title : To find windchill
/**********************************************************************************
'''
import math

def windchill():
    """
    Description:
        This function takes takes temperature and speed as input and
        caculates windchill with given formula.     
    """
    temperature = float(input("Enter temp t: "))
    speed = float(input("Enter speed v: "))
    # validation for temperature
    if (temperature > 50):
        print("Temperature should be less than 50.")
        windchill()
        return
    # validation for speed
    if (3 > speed) or (speed > 120):
        print("Speed should be less than 120 and greater than 3.")
        windchill()
        return
    # formula for windchill
    wind_chill = 35.74 + 0.6215 * temperature + (
        0.4275 * temperature - 35.75
        ) * math.pow(speed, 0.16)
    
    print("wind chill: ", round(wind_chill, 2))

windchill()