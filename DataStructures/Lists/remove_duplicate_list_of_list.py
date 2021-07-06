'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to remove duplicate elements from list of list.
/**********************************************************************************
'''
import logging
from logging_handler import logger
import itertools

def remove_duplicate_list_of_list():
    """
    Description:
        This function will remove duplicate elements from list of list..
    """
    number_list= [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    try:
        number_list.sort()
        new_number_list = list(num for num,_ in itertools.groupby(number_list))
        logger.info(f"New List {new_number_list}")
    except Exception as e:
        logger.info(f"Error!! {e}")

remove_duplicate_list_of_list()