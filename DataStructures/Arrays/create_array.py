'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Display Array Elements
/**********************************************************************************
'''
import logging
from logging_handler import logger
class Array():

    def display_array_elements(self):
        """
        Description:
            This function prints array of 5 numbers and disply its elements. 
        """
        try:
            # creating array with list comprehension
            int_array = [x for x in range(5)]
            logger.info(int_array)
            # printing array elemets by iterating with for loops
            for i in range(len(int_array)):
                logger.info(int_array[i])
            # printing array elements with index
            logger.info(int_array[3])
        except Exception as e:
            logger.info(f"Error {e}")

disply_array = Array()
disply_array.display_array_elements()