'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to create intersection of sets.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def intersect_sets():
    """
    Description:
        This function will intersect two sets. 
    """
    my_set = {1,2,3,4,5}
    new_set = {6,7,8,9,1,2,3}
    try:
        # use intersection() method to get intersection of two sets
        intersection_set = set((my_set.intersection(new_set)))
        logger.info(f"Set after intersection: {intersection_set}")
    except Exception as e:
        logger.info(f"Error! {e}")

intersect_sets()