'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Count the number values associated with key in dictionary.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def values_associated():
    """
    Description:
        This function prints values associated with keys in dictionary.
        it counts the number of times success appreared true in dictionaries. 
    """
    student = [{'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': True, 'name': 'Alex'}]
    try:
        success_count= (sum(d['success'] for d in student))
        logger.info(f"number of times success appreaed as true is: {success_count}")
    except Exception as e:
        logger.info(f"Error!!!{e}")

values_associated()