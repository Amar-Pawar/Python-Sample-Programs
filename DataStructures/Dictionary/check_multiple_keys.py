'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-05
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-05
@Title : Check multiple keys in dictionary.
/**********************************************************************************
'''
import logging
from logging_handler import logger

def multiple_keys():
    """
    Description:
        This function checks if mutiple keys are preset in dictionary or not. 
    """
    person_dict = {"name":"Amar", "age":27,"Id":1,"Profession":"Engineer"}
    try:
        check_keys={"name","age"}
        if(person_dict.keys()) >= check_keys:
            logger.info("All keys are present")
        else:
            logger.info("All keys are not present")
    except Exception as e:
        logger.info(f"Error!! {e}")

multiple_keys()