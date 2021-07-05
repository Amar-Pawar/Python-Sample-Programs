'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : To get number of occurances of specific elements in array
/**********************************************************************************
'''
from collections import Counter
import logging
from logging_handler import logger


class Array():
    def count_elements(self):
        """
        Description:
            This function prints occurances of specific elements in array by using counter() function
            imported from python collections.
        """
        try:
            array_list = ["1", "5", "5", "5", "1"]
            # using counter to get occurances
            occurrences = Counter(array_list)
            logger.info(occurrences)
            logger.info(occurrences["5"])
        except Exception as e:
            logger.info(f"Error {e}")

counter = Array()
counter.count_elements()
