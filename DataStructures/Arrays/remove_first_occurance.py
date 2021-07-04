'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : To remove first occurance of specific element from an array.
/**********************************************************************************
'''
import logging
from logging_handler import logger

class Array():
    def remove_element(self):
        """
        Description:
            This function removes first occurance of specific element from array.
        """
        array = [1,5,10,1,9,1,44]
        array.remove(1)
        logger.info(array)

remove_element = Array()
remove_element.remove_element()