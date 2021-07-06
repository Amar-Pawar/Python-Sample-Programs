'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to append one list to other.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def append_list():
    """
    Description:
        This function will append one list to other.
    """
    list1 = [1, 2, 3, 4]
    list2 = [5,6,7,8]
    try:
        list1.extend(list2)
        logger.info(f"List after appending: {list1}")
    except Exception as e:
        logger.info(f"Error!! {e}")

append_list()