'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Print list as key with nested dictionary.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def list_to_dict():
    """
    Description:
        This function prints list as keys with nested dictionaries. 
    """
    name_list = ["Amar", "sagar", "sanket", "swaraj"]
    try:
        dict = current = {}
        for name in name_list:
            current[name] = {}
            current = current[name]
        logger.info(f"dictionary with nested keys: {dict}")
    except Exception as e:
        logger.info(f"Error!! {e}")

list_to_dict()