'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-25
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-25
@Title : To replace given string
/**********************************************************************************
'''
def string_replace():
    username = input("enter Username - ")
    # check if username have minimum 3 characters
    if len(username) > 3:
        string_template = f"Hello {username}, How are you?" #string formating
        return string_template
    else:
        print("Username should be of 3 characters")
        string_replace()

final_string = string_replace()
print(final_string)
