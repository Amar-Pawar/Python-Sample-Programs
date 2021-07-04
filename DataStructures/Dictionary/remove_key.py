'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Remove key from dictionary
/**********************************************************************************
'''
import logging
from logging_handler import logger

def remove_key():
    """
    Description:
        This function remove key from dictionary. 
    """
    dict1 =  {'1':10,'2':20,'3':30,'4':40}
    #del dict1['4']
    dict1.pop('3') # using pop() method to remove key
    logger.info(f"Dictionary after removing key {dict1}")

remove_key()