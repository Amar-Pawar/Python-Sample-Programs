'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to remove element from set.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def remove_element():
    """
    Description:
        This function will remove element from set. 
    """
    my_set = {1,2,3,4,5}
    try:
        # by remove() function
        my_set.remove(1)
        logger.info(f"Set after removing element: {my_set}")

        # by discard() method
        my_set.discard(5)
        print(f"Set after removing element: {my_set}")
    except Exception as e:
        logger.info(f"Error!! {e}")

remove_element()