'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-06
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-06
@Title : Check if lists are cicularly identical.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def circularly_identical():
    """
    Description:
        This function will Check if lists are cicularly identical.
    """
    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    list3 = [1, 10, 10, 0, 0]
    try:
        # doubling list
        list1.extend(list1) 
        # traversal in twice of list1
        for i in range(len(list1)):
            # check if sliced list1 is equal to list2
            if list2 == list1[i: i + len(list2)]:
                return True
        return False
    except Exception as e:
        logger.info(f"Error!! {e}")

logger.info(circularly_identical())

    