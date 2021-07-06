'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Convert list into tuple
/**********************************************************************************
'''
import logging
from logging_handler import logger

def conver_list_to_tuple():
    """
    Description:
        This function will convert list into tuple.
    """
    # tuple with mixed datatypes
    my_list = [1, "Amar", 2.5]
    try:
        my_tuple = tuple(my_list)
        logger.info(f"list after converting in tuple {my_tuple}")
    except Exception as e:
        logger.info(f"Error!! {e}")

conver_list_to_tuple()