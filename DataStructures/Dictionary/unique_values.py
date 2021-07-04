'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Print unique values from dictionary
/**********************************************************************************
'''
import logging
from logging_handler import logger

def unique_values():
    """
    Description:
        This function is to print unique values from dictionary. 
    """
    dict1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    unique_value = set( value for dic in dict1 for value in dic.values())
    logger.info(f"Unique Values: {unique_value}")

unique_values()
