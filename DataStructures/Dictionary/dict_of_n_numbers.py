'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Generate and print dictionary between 1 to n number as key n*n as value.
/**********************************************************************************
'''
import re
import logging
from logging_handler import logger

def dict():
    """
    Description:
        This function generates and print dictionary between 1 to n numbers as key and 
        n*n as value. 
    """
    n = int(input("Input a number "))
    pattern = re.compile("^[1-9]{1}$")
    if re.match(pattern,str(n)):
        pass
    else:
        print("Enter single digit number ")
        dict()
    my_dict ={}

    for x in range(1,n+1):
        my_dict[x]=x*x

    logger.info(my_dict)
dict()