'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Add key to dictionary.
/**********************************************************************************
'''
from logging_handler import logger

class Dictionary():

    def add_key(self):
        """
        Description:
            This function adds new key to dictionary. 
        """
        dict = {'1':10,'2':20}
        dict['3']=30
        logger.info(f"Dictionary after adding new key: {dict}")

new_key = Dictionary()
new_key.add_key() 