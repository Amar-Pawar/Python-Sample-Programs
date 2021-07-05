'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Count number of items in dictionary values that are in list.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def count_list_value_items():
    """
    Description:
        This function counts number of items in dictionary values that are in list
        This function uses list comprehension to loop over items. 
    """
    dict = {'first' : [12, 52, 33, 74, 15, 6, 97],
            'second' : 1,
            'third' : 11,
            'fourth' : [72, 98, 59, 76, 44] 
            }
    try:
        count_elements = (sum([len(dict[x]) for x in dict if isinstance(dict[x], list)]))
        logger.info(f"Total number of items present in list as values in dict: {count_elements}")
    except Exception as e:
        logger.info(f"Error!! {e}")
    
count_list_value_items()