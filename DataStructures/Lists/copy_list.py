'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to copy list.
/**********************************************************************************
'''
import logging
from logging_handler import logger
import copy

def copy_list():
    """
    Description:
        This function will copy given list.
    """
    list1 = [1, 2, 3, 4]
    try:
        # using copy for shallow copy  
        copied_list = copy.copy(list1)
        logger.info(f"List after copying: {copied_list}")
    except Exception as e:
        logger.info(f"Error!! {e}")

copy_list()