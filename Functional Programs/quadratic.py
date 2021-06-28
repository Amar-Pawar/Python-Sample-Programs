'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-28
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-28
@Title : To find the root of equation
/**********************************************************************************
'''
import math

def quadratic():
    """
    Description:
        This function takes takes three integers as input in expression and 
        evaluates roots of given equation.     
    """
    print("Enter values of a, b, c - ")
    a = int(input("a "))
    b = int(input("b "))
    c = int(input("c "))
    delta = (b * b) - (4 * a * c)  # in provided formulas to calculate roots of given equation

    try:
        first_root = (-b + math.sqrt(abs(delta))) / (2 * a)
        second_root = (-b - math.sqrt(abs(delta))) / (2 * a)
    except Exception as ZeroDivisionError:
        print("Please enter non zero value of a.")
        quadratic()
        return

    print(round(first_root, 2), " ", round(second_root, 2))

quadratic()