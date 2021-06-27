'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-27
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-27
@Title : To find distinct triplet whoes addition is zero
/**********************************************************************************
'''

def distance():
    """
    Description:
        This function takes x and y co-ordinates as input and calculate its distance from origin.     
    """
    x_co_ordinate = int(input("Enter x co-ordinate: "))
    y_co_ordinate = int(input("Enter y co-ordinate: "))
    dist = pow((x_co_ordinate * x_co_ordinate + y_co_ordinate * y_co_ordinate), 0.5)  # in formula : square root of (x*x+y*y)
    print("Euclidean distance is: ", round(dist, 2))

distance()