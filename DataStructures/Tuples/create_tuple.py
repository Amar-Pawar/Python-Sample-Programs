'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Create a tuple
/**********************************************************************************
'''
import logging
from logging_handler import logger

def create_tuple():
    """
    Description:
        This function will print different types of tuples.
    """
    # Empty tuple
    my_tuple = ()
    logger.info(my_tuple)

    # Tuple having integers
    my_tuple = (1, 2, 3)
    logger.info(my_tuple)

    # tuple with mixed datatypes
    my_tuple = (1, "Amar", 2)
    logger.info(my_tuple)

    # nested tuple
    my_tuple = ("Amar", [11, 3, 6], (22, 52, 33))
    logger.info(my_tuple)

create_tuple()