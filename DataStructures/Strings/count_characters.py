'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Calculate count of character frequency
/**********************************************************************************
'''
import logging
from logging_handler import logger
from collections import Counter

def count_character_frequency():
    """
    Description:
        This function will calculate count of character frequency.
    """
    my_string = "Amaar"
    try:
        count_char = Counter(my_string)
        logger.info(f"character frequency: {count_char}")
    except Exception as e:
        logger.info(f"Error!! {e}")

count_character_frequency()