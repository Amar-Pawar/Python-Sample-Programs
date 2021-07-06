'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to check if two list contain atleast one common member.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def common_member():
    """
    Description:
        This function will check if two list contain atleast one common member.
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = [5,6, 7, 8, 9]
    try:
        list1_set = set(list1)
        list2_set = set(list2)
        if len(list1_set.intersection(list2_set)) > 0:
            logger.info(True)
        else:
            logger.info(False)
    except Exception as e:
        logger.info(f"Erroe!! {e}")

common_member()