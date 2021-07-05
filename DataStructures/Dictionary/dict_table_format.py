'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Print dictionary in table format.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def dict_in_table():
    """
    Description:
        This function prints dictionary in table format. 
    """
    dict = {1: ["Amar", 27, 'Engineer'],
        2: ["Swaraj", 27, 'HR'],
        3: ["Yogesh", 29, 'Manager'],
        4: ["Sanket", 25, 'Finance'],
        }
    try:
        logger.info("{:<8} {:<15} {:<10} {:<10}".format('ID','Name','Age','Department'))
        for k, v in dict.items():
            name, age, department = v
            logger.info("{:<8} {:<15} {:<10} {:<10}".format(k, name, age, department))
    except Exception as e:
        logger.info(f"Error!! {e}")

dict_in_table()