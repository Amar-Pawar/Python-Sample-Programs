'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-25
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-25
@Title : To find the prime factors of given number
/**********************************************************************************
'''
def find_factors():
    number = int(input("Enter Number - "))
    factor = 2
    factor_string = ""
    for factor_number in range(2,number):
        if factor_number*factor_number<=number:
            while(number%factor_number == 0):
                factor_string += f"{str(factor)} "
                number = int(number/factor_number)

    if number > 2:
        factor_string += f"{str(number)} "
    else:
        pass
    print(factor_string)

find_factors()