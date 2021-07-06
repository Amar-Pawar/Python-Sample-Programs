'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Program to reverse a tuple.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def reverse_tuple():
    """
    Description:
        This function will reverse a tuple and print it.
    """
    try:
        my_tuple = (1, "Amar", 2.5)
        reversed_tuple = reversed(my_tuple)
        logger.info(tuple(reversed_tuple))
    except Exception as e:
        logger.info(f"Error!! {e}")

reverse_tuple()