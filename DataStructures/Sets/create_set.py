'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to create a set.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def create_set():
    """
    Description:
        This function is to create set. 
    """
    my_set = {1,2,3,4,5}
    logger.info(f"Set created is: {my_set}")

    # creating set by built in function set()
    new_set = set([1,2,3,5])
    logger.info(f"Set created is: {new_set}")

create_set()
