'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Iterate over dictionary.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def iterate_dict():
    """
    Description:
        This function iterates over dictionary by for loop. 
    """
    dict1 =  {'1':10,'2':20,'3':30,'4':40}
    for key,value in dict1.items():
        logger.info("{}, {}".format(key,value))

iterate_dict()