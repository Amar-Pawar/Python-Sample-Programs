'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to get difference between two list.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def diffrence_between_lists():
    """
    Description:
        This function will give difference between list by set().
    """
    list1 = [1,2,3,4,5]
    list2 = [1,2,6,7,8]
    try:
        # converting lists into set for given operation
        set_list1 = set(list1)
        set_list2 = set(list2)
        # get difference between two list by sets
        diff1= list(set_list1.difference(set_list2))
        diff2= list(set_list2.difference(set_list1))
        total_diff = diff1 + diff2
        logger.info(total_diff)
    except Exception as e:
        logger.info(f"Error! {e}")

diffrence_between_lists()