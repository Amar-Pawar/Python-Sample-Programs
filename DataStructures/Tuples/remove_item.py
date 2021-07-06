'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Remove item from a tuple.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def remove_item():
    """
    Description:
        This function will remove item from tuple.
    """
    my_tuple = (1, "Amar", 2.5, 50)
    try:
        # removing item by slicing technique
        my_tuple = my_tuple[:1] + my_tuple[2:]
        logger.info(my_tuple)
        # removing item by converting in list
        my_list = list(my_tuple)
        my_list.remove(1)
        logger.info(tuple(my_list))
    except Exception as e:
        logger.info(f"Error!!{e}")

remove_item()