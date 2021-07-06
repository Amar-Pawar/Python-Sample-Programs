'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to find sum of all elements in list.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def list_sum():
    """
    Description:
        This function will get total sum of all elements in list. 
    """
    list = [11,45,12,43,76]
    try:
        total = sum(list) # using sum() method
        logger.info(f"Total of all elements in list is: {total}")
    except Exception as e:
        logger.info(f"Error!! {e}")

list_sum()