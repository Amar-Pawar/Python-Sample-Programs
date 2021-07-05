'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to remove element from set if it is present.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def remove_element():
    """
    Description:
        This function will remove element from set if it is present. 
    """
    my_set = {1,2,3,4,5}
    try:
        # use remove() method to remove elemnet present in set
        my_set.remove(1)
        logger.info(f"Set after removing element: {my_set}")
    except Exception as e:
        logger.info("Element not present")

remove_element()