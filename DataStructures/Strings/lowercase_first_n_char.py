'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Program to lowercase first n characters of string.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def lower_n_char():
    """
    Description:
        This function will lowercase first n characters of string.
    """
    my_string = "AMARPawar"
    try:
        new_string = my_string[:3].lower() + my_string[3:]
        logger.info(f"lengt of given string is: {new_string}")
    except Exception as e:
        logger.info(f"Error!! {e}")

lower_n_char()