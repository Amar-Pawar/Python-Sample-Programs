'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Find all permutations of list.
/**********************************************************************************
'''
import logging
from logging_handler import logger
from itertools import permutations
def permutation():
    """
    Description:
        This function will find all permutations of list elements using permutations() method.
    """
    list1 = list(permutations(range(1, 3)))
    logger.info(list1)
    
permutation()

