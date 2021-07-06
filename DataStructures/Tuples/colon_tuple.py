'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Create colon of tuple.
/**********************************************************************************
'''
import logging
from logging_handler import logger
from copy import deepcopy

def colon_tuple():
    """
    Description:
        This function will create colon of tuple.
    """
    my_info = ("Amar", 27, "Engineer", []) 
    try:
        #make a copy of a tuple using deepcopy() function
        my_info_colon = deepcopy(my_info)
        my_info_colon[3].append(50000)
        logger.info(my_info_colon)
        logger.info(my_info)
    except Exception as e:
        logger.info(f"Error!! {e}")

colon_tuple()