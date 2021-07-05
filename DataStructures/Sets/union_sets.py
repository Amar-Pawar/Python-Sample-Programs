'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to create union of sets.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def union_sets():
    """
    Description:
        This function will give union of two sets. 
    """
    my_set = {1,2,3,4,5}
    new_set = {6,7,8,9,1,2,3}
    try:
        # use union() method to get intersection of two sets.
        # it neglects duplicate entries as sets doesnt store duplicate values.
        union_set = my_set.union(new_set)
        logger.info(f"Set after union: {union_set}")
    except Exception as e:
        logger.info(f"Error! {e}")

union_sets()