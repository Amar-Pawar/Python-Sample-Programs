'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Program to slice tuple.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def slice_tuple():
    """
    Description:
        This function will slice a tuple and print it.
    """
    my_tuple = (1, "Amar", 2.5, 50, "sanket", 22, "swaraj")
    try:
        sliced_tuple = my_tuple[:2]
        logger.info(f"Tuple after slicing: {sliced_tuple}")
    except Exception as e:
        logger.info(f"Error!!{e}")

slice_tuple()