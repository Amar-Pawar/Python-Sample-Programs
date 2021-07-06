'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Create a tuple with differnet datatypes
/**********************************************************************************
'''
import logging
from logging_handler import logger

def create_tuple():
    """
    Description:
        This function will create and print tuple with diffrent data types.
    """
    # tuple with mixed datatypes
    my_tuple = (1, "Amar", 2.5)
    logger.info(my_tuple)

create_tuple()