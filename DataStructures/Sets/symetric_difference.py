'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to find symmetric diffrence in sets.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def symmetric_difference():
    """
    Description:
        This function will give symmetric difference of two sets. 
    """
    my_set = {1,2,3,4,5}
    new_set = {6,7,8,9,1,2,3}
    try:
        # use symmetric_difference() method to get symmetric difference of two sets.
        # it will give unique value that are not present in each other
        symmetric_difference_set = my_set.symmetric_difference(new_set)
        logger.info(f"Symmetric difference in sets: {symmetric_difference_set}")
    except Exception as e:
        logger.info(f"Error! {e}")

symmetric_difference()