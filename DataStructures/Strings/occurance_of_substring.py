'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Count the occurance of substring in string.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def count_substring_occurance():
    """
    Description:
        This function will count the occurance of substring in string.
    """
    my_string = "His name is Amar, Amar likes to play cricket"
    try:
        occurance_substring = my_string.count("Amar")
        logger.info(f"Number of times substring occurred: {occurance_substring}")
    except Exception as e:
        logger.info(f"Error!! {e}")

count_substring_occurance()