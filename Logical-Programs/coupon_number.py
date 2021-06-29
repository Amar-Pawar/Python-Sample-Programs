'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-29
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-29
@Title : To find total random number generated to get dinstinct coupon number
/**********************************************************************************
'''
import random

def coupon():
    """
    Description:
        This function takes coupen number as input and calculates total number of
        random number generated to get distinct coupon number.     
    """
    # take input for coupon number
    coupon_number = input("enter coupon number: ")  
    count = 0  
    # suppose it is 25. typecast it in int i.e input string 25 will be int 2 and 5 in the form of list
    num = [int(i) for i in str(coupon_number)] 
    print(num)  
    while len(num) > 0:  
        # generate random number between 0-9 and
        random_no = random.randint(0, 9)  
        # increment the count by 1.
        count += 1  
        # but if is repeated remove that number from list
        if random_no in num:
            num.remove(random_no)
    print("total number of  random numbers to generate coupon: ", count)

coupon()
