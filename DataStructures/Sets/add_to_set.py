'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to  add new element in a set.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def add_to_set():
    """
    Description:
        This function will add new member to set. 
    """
    number_set = {1,2,3,4,5}
    try:
        number_set.add(10)
        logger.info(f"Set after adding new element: {number_set}")
    except Exception as e:
        logger.info(f"Error!! {e}")

add_to_set()