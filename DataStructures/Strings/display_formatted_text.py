'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title: Display formatted text as output
/**********************************************************************************
'''
import logging
from logging_handler import logger
import textwrap

def display_formated_text():
    """
    Description:
        This function will Display formatted text as output.
    """
    my_info = """My name is Amar Pawar. I live in Pen which locates in raigad district.
    I like to play different types of sports like cricket, badminton, football, carrorm.
    I have studied in Mumbai University"""
    try:
        formatted_text = textwrap.fill(my_info, width=50)
        logger.info(f"formatted text: {formatted_text}")
    except Exception as e:
        logger.info(f"Error!! {e}")

display_formated_text()