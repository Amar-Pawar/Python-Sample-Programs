'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to find diffrence in sets.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def sets_difference():
    """
    Description:
        This function will give difference two sets. 
    """
    my_set = {1,2,3,4,5}
    new_set = {6,7,8,9,1,2,3}
    try:
        # use difference() method to get intersection of two sets.
        difference_set = my_set.difference(new_set)
        logger.info(f"Difference in sets: {difference_set}")
    except Exception as e:
        logger.info(f"Error! {e}")

sets_difference()