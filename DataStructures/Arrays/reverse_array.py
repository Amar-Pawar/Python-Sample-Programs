'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Display array elements in reverse order.
/**********************************************************************************
'''
import logging
from logging_handler import logger

class Array():
    def reverse_array_items(self):
        """
        Description:
            This function prints array elements in reverse order using reverse() method.
        """
        # creating array with list comprehension
        int_array = [x for x in range(5)]
        # using reverse() method to print elements in reverse order
        int_array.reverse()
        logger.info(int_array)

reverse_array = Array()
reverse_array.reverse_array_items()