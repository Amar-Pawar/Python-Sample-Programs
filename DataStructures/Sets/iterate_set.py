'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to iterate over set.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def iterate_set():
    """
    Description:
        This function will iterate over the set. 
    """
    # for character set
    my_set= set("Amar")
    result = [logger.info(x) for x in my_set] # by comprehension
    # for number set iterating with for loop
    num_set ={1,2,3,4}
    for i in num_set:
        logger.info(i)

iterate_set()