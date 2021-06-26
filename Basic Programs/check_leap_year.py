'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-25
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-25
@Title : To check if year is leap year or not
/**********************************************************************************
'''
def check_leap_year():
    year = input("Enter year - ")
    #check length of given year
    if len(year) == 4:
        #check if year is divisible by 4
        if int(year) % 4 == 0:
            print(year, " is a leap year")
        else:
            print(year, " is not leap year")
    else:
        print("please enter 4 digit number as year")
        check_leap_year()

check_leap_year()


    