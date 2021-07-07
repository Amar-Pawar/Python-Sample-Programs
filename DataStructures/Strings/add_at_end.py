'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Add 'ing' or 'ly' at end of string according to length
/**********************************************************************************
'''
import logging
from logging_handler import logger

def add_string_at_end():
    """
    Description:
        This function will add 'ing' or 'ly' at end of string according to length.
    """
    my_string = "Amar"
    try:
        length = len(my_string)
        if length > 2:
            if my_string[-3:] == 'ing':
                my_string += 'ly'
            else:
                my_string += 'ing'
        logger.info(f"lengt of given string is: {my_string}")
    except Exception as e:
        logger.info(f"Error!! {e}")

add_string_at_end()
