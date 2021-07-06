'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title: Unpack tuple in different variables
/**********************************************************************************
'''
import logging
from logging_handler import logger

def unpack_tuple():
    """
    Description:
        This function will unpack tuple in different variables.
    """
    my_info = ("Amar", 27, "Engineer") 
    try:
        # unpacking tuple in below variables
        name, age, profession = my_info
        # printing variables after unpacking tuple
        logger.info(name)
        logger.info(age)
        logger.info(profession)
    except Exception as e:
        logger.info(f"Error!!{e}")

unpack_tuple()