'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Check if element is present or not in tuple.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def check_element():
    """
    Description:
        This function will check if element is present or not in tuple.
    """
    my_tuple = (1, "Amar", 2.5)
    try:
        result = ("Amar" in my_tuple)
        logger.info(result)
    except Exception as e:
        logger.info(f"Error!!{e}")

check_element()