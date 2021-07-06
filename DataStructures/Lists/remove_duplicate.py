'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to remove duplicate elements in list.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def remove_duplicate():
    """
    Description:
        This function will remove duplicate elements in list.
    """
    list = [2, 4, 10, 20, 5, 2, 20, 4]
    final_list = []
    try:
        for num in list:
            if num not in final_list:
                final_list.append(num)
        print(final_list)
    except Exception as e:
        logger.info(f"Error!! {e}")
        
remove_duplicate()