'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to find minimum and maximum value in set.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def find_min_max():
    """
    Description:
        This function will find min and max element in set. 
    """
    number_set = {11,78,45,34,98}
    try:
        # finding min value
        min_value = min(number_set)
        # finding max value
        max_value = max(number_set)
        logger.info(f"Minimum value in set is {min_value} and max value in set is {max_value}")
    except Exception as e:
        logger.info(f"Error!! {e}")

find_min_max()