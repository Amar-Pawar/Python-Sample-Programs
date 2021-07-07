'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Display string input in upper and lower case
/**********************************************************************************
'''
import logging
from logging_handler import logger

def to_lower_upper_case():
    """
    Description:
        This function will display string input in upper and lower case.
    """
    my_string = input("Enter any string: ")
    try:
        to_lower_case = my_string.lower()
        to_upper_case = my_string.upper()
        logger.info(f"Input string in lower case: {to_lower_case}")
        logger.info(f"Input string in upper case: {to_upper_case}")
    except Exception as e:
        logger.info(f"Error!! {e}")

to_lower_upper_case()