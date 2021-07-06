'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Program to find product of all elements in list.
/**********************************************************************************
'''
import logging
from logging_handler import logger
import math

def list_product():
    """
    Description:
        This function will get product of all elements in list. 
    """
    list = [1,2,3,4,5]
    try:
        product_list = math.prod(list) # using sum() method
        logger.info(f"Product of all elements in list is: {product_list}")
    except Exception as e:
        logger.info(f"Error!! {e}")

list_product()