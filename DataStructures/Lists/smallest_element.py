'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to find smallest elements in list.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def smallest_element():
    """
    Description:
        This function will give smallest elements in list. 
    """
    list = [1,2,3,4,5]
    try:
        smallest_number = min(list) # using sum() method
        logger.info(f"smallest of all elements in list is: {smallest_number}")
    except Exception as e:
        logger.info(f"Error!! {e}")

smallest_element()