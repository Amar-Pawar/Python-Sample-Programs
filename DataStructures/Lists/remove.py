'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to remove elements from given index in list.
/**********************************************************************************
'''
import logging
from logging_handler import logger
import copy

def remove():
    """
    Description:
        This function will remove elements from given index in list.
    """
    list1 = ["Amar", "sagar", "sanket", "nishad", "swaraj", "mayur"]
    try:
        list1 = [x for (i,x) in enumerate(list1) if i not in (0,4,5)]
        logger.info(f"List after removing elements at given position: {list1}")
    except Exception as e:
        logger.info(f"Error!! {e}")

remove()