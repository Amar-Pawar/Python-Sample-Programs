'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Sort unique words from collection of words sepereated by commas ,alphanumarically
/**********************************************************************************
'''
import logging
from logging_handler import logger

def sort_unique_words():
    """
    Description:
        This function will sort unique words from collection of words sepereated by commas ,alphanumarically.
    """
    try:
        items = input("Input comma separated sequence of words: ")
        words = [word for word in items.split(",")]
        unique_words = (",".join(sorted(list(set(words)))))
        logger.info(f"lengt of given string is: {unique_words}")
    except Exception as e:
        logger.info(f"Error!! {e}")

sort_unique_words()