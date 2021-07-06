'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to get count of specified mentioned string type in list.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def compare():
    """
    Description:
        This function will give count of specified mentioned string type in list.. 
    """
    counter = 0
    a = ['abc', 'xyz', 'aba', '1221', 'aaa']
    try:
        for i in a:
            if len(i) > 1 and i[0] == i[-1]:
                counter+= 1
        logger.info(f"Number of time specified string occuraed: {counter}")
    except Exception as e:
        logger.info(f"Error!! {e}")

compare()

