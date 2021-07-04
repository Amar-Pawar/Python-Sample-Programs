'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Concatinate three dictionaries.
/**********************************************************************************
'''
import logging
from logging_handler import logger

class Dictionary():

    def concate_dict(self):
        """
        Description:
            This function concatinates dictionaiesy. 
        """
        dict1 =  {'1':10,'2':20}
        dict2 =  {'3':30,'4':40}
        dict3 =  {'5':50,'6':60}

        # using "|" operator to merge dictionaries
        concatinated_dict = dict1 | dict2 | dict3
        logger.info(concatinated_dict)
    
concat = Dictionary()
concat.concate_dict()