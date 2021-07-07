'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Program to reverse string
/**********************************************************************************
'''
import logging
from logging_handler import logger

def reverse_string():
    """
    Description:
        This function will reverse string.
    """
    my_string = "Amar"
    try:
        reverse_string = my_string[::-1]
        logger.info(f"String after reversing: {reverse_string}")
    except Exception as e:
        logger.info(f"Error!! {e}")

reverse_string()