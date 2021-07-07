'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Change all occurance of first char to $ except first char in string
/**********************************************************************************
'''
import logging
from logging_handler import logger

def change_occurance():
    """
    Description:
        This function will change all occurance of first char to $ except first char in string.
    """
    my_string = "amar"
    try:
        char = my_string[0]
        my_string = my_string.replace(char, '$')
        my_string = char + my_string[1:]
        logger.info(f"String after changing occurance: {my_string}")
    except Exception as e:
        logger.info(f"Error!! {e}")

change_occurance()
