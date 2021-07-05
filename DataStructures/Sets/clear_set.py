'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to clear set.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def clear_set():
    """
    Description:
        This function will clear all elements from set. 
    """
    my_set = {"Amar", "Sagar", "Mayur", "Sanket"}
    try:
        my_set.clear()
        logger.info(f"Set after clearing all element: {my_set}")
    except Exception as e:
        logger.info(f"Error!! {e}")

clear_set()