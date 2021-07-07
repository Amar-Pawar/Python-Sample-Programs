'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Calculate length of string
/**********************************************************************************
'''
import logging
from logging_handler import logger

def length_string():
    """
    Description:
        This function will calculate length of string.
    """
    my_string = "Amar"
    try:
        length = len(my_string)
        logger.info(f"lengt of given string is: {length}")
    except Exception as e:
        logger.info(f"Error!! {e}")

length_string()
