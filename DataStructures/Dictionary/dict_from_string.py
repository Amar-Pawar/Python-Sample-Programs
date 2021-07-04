'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Create dictionary from string
/**********************************************************************************
'''
import logging
from logging_handler import logger
from collections import defaultdict, Counter

def dict_from_string():
    """
    Description:
        This function will create dictionary from string. 
    """
    str1 = 'amarboyop' 
    my_dict = {}
    for letter in str1:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    logger.info(my_dict)
    
dict_from_string()