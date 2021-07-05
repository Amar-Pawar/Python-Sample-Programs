'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-04
@Title : Sort dictionary in ascending and descending order.
/**********************************************************************************
'''

from collections import OrderedDict
import logging
from logging_handler import logger

class Dictionary():
  
    def __init__(self):
        self.person= {'name':'Amar', 'age':"pqr", 'profession':'Engineer'}

    def ordered_dict(self):
        """
        Description:
            This function prints dictionary in ascending order by keys using orderdDictionary. 
        """
        dict1 = OrderedDict(sorted(self.person.items()))
        logger.info(f"dictionary ordered by keys {dict1}")

    def decsending_sort(self):
        """
        Description:
            This function prints dictionary in descending order by values. 
        """
        # sort by value
        try:
            desc_sort= (sorted(self.person.items(), key =
                        lambda kv:kv[1], reverse=True))
            logger.info(f"Dictionary sorted in descending order by values: {desc_sort}")

            #seperating elements            
            for i in desc_sort:
                logger.info("{},{}".format(i[0],i[1]))
        except Exception as e:
            logger.info(f"Error!!!{e}")
                
    def ascending_sort(self):
        """
        Description:
            This function prints dictionary in ascending order by values. 
        """
        # ascending order
        try:
            asc_sort= (sorted(self.person.items(), key =
                        lambda kv:kv[1]))
            logger.info(f"Dictionary elements in ascending order by values: {asc_sort}")
            # sepersting elements
            for i in asc_sort:
                logger.info("{},{}".format(i[0],i[1]))
        except Exception as e:
            logger.info(f"Error!!{e}")

dict = Dictionary()
dict.ordered_dict()
dict.decsending_sort()
dict.ascending_sort()