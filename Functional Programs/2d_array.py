'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-27
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-27
@Title : 2d array
/**********************************************************************************
'''

def two_d_array():
    """
    Description:
        This function prints 2d array. It takes number of rows and colums
        as well as values of array from user.    
    """

     # take number of rows and columns fom user
    num_of_rows = int(input("enter number of rows: "))
    num_of_columns = int(input("enter number of columns: "))
    final_array = []
    for i in range(0,num_of_rows):
        final_array.append([])

    for i in range(0, num_of_rows):
        for j in range(0, num_of_columns):
            num = int(input(f"enter value for row {i} column {j} "))
            final_array[i].append(num)
    print(final_array)
two_d_array()