'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Find longest word in list of words
/**********************************************************************************
'''
import logging
from logging_handler import logger

def longestLength(a):
    """
    Description:
        This function will Find longest word in list of words.
    """
    try:
        max1 = len(a[0])
        temp = a[0]
    
        for i in a:
            if(len(i) > max1):
                max1 = len(i)
                temp = i
        logger.info(f"The word with the longest length is: {temp} and length is:  {max1}")
    except Exception as e:
        logger.info(f"Error!! {e}")

my_list = ["one", "two", "third", "four"]
longestLength(my_list)
