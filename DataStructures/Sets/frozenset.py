'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Program to use frozensets.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def frozen_sets():
    """
    Description:
        This function uses frozen sets to store keys of dictionary. 
    """
    # creating a dictionary
    person_dict =   {
                    "name": "Amar", 
                    "age": 27, 
                    "sex": "Male", 
                    "profession": "Engineer"
                    }

    # making keys of dictionary as frozenset
    key = frozenset(person_dict)
    logger.info(f"The frozen set is: {key}")

frozen_sets()