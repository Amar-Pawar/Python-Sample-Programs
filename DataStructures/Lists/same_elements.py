'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to print common elements from two lists.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def common_elements():
    """
    Description:
        This function will print common elements in both list.
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = [5,6, 7, 8, 9]
    try:
        list1_set = set(list1)
        list2_set = set(list2)
        if len(list1_set.intersection(list2_set)) > 0:
            logger.info(list1_set.intersection(list2_set))
        else:
            logger.info("No common elements")
    except Exception as e:
        logger.info(f"Error!! {e}")

common_elements()