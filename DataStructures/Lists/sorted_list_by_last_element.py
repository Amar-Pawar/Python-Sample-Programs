'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Sort list by last element in tupple.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def sort_list_last():
    """
    Description:
        This function will sort the elements in tuple inside list accoprding to last element. 
    """
    list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    try:
        list1.sort(key= lambda x:x[-1])
        logger.info(f"list after sorting: {list1}")
    except Exception as e:
        logger.info(f"Error!! {e}")
        
sort_list_last()

