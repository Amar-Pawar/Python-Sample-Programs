'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Find repeated elements in tuple.
/**********************************************************************************
'''
import logging
from logging_handler import logger
from collections import Counter

def repeated_items():
    """
    Description:
        This function will find repeated items in tuple.
    """
    number_tuple = (1,1,1,2,3,4,4,4,5,6,6,7,7,8,9)
    try:
        duplicate_entries = Counter(number_tuple)
        logger.info(duplicate_entries)
        
        repeated_tuple = tuple([item for item in duplicate_entries if duplicate_entries[item]>1])
        logger.info(repeated_tuple)
    except Exception as e:
        logger.info(f"Error!! {e}")

repeated_items()