'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-30
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-30
@Title : Addressbook System
/**********************************************************************************
'''

import json
import logging
import re

logging.basicConfig(filename='contact.log', level=logging.INFO)

class Addressbook():
    # creating a constructor
    def __init__(self):
        print("Welcome To Addressbook System")
    # main method to call other functions
    def main(self):
        """
        Description:
            This is main function it will call other methods to execute.
            It will ask user to make choice and accordingly call methods
        """

        print("Enter 1. To add contact")
        
        choice = int(input("Enter your choice: "))
        try:
            with open('addressbook.json', 'r') as f:
                address_dict = json.load(f)
        except Exception as e:
            print("File not found")
            return

        if choice==1:
            address_json = self.add_contact(address_dict)
        else:
            print("Invalid choice!! Please enter correct input")
            self.main()

        print("Do you want to try again? 1.Yes  2.No")
        choice = int(input())
        if choice == 1:
            self.main()
        else:
            return

    # function to add new contact   
    def add_contact(self, address_dict):
        """
        Description:
            This function is to add contact to addressbook. It asks user for inputs for
            different fields to store in addressbook and stores it in json file
        Parameters:
            It takes address_dict as parameter where we have loaded json file
        Return:
            It return addressbook dictionary
        """

        final_address_dict = {}
        address_json = address_dict['address']
        #validating name with regex   
        name = input("Enter your name ")
        pattern = re.compile("^[A-Za-z]{3,}$")
        if re.match(pattern,name):
            pass
        else:
            print("Name should contain only letters ans min 3 characters Example: Amar")
            name=input("Enter your name ")
        # validating address with regex
        address = input("Enter home address ")
        pattern = re.compile("^[A-Z0-9\sa-z]*$")
        if re.match(pattern,address):
            pass
        else:
            print("Enter proper address")
            address=input("Enter your address ")
        # validating city
        city = input("Enter city name ")
        pattern = re.compile("^[A-Za-z]*$")
        if re.match(pattern,city):
            pass
        else:
            print("Enter proper city name.Example: Mumbai")
            city = input("Enter city name ")
        # validating zip code
        zip_code = input("Enter zipcode ")
        pattern = re.compile("^[1-9]{1}[0-9]{5}$")
        if re.match(pattern,zip_code):
            pass
        else:
            print("Enter proper 6 digit zip code. Example: 402107")
            zip_code = input("Enter zipcode ")
        # validating state name
        state = input("Enter state ")
        pattern = re.compile("^[A-Za-z]*$")
        if re.match(pattern,state):
            pass
        else:
            print("Enter proper state name. Example: Maharashtra")
            state = input("Enter state ")
        # validating phone number
        number = input("Enter your number ")
        pattern = re.compile("^[7-9]{1}[0-9]{9}$")
        if re.match(pattern,number):
            pass
        else:
            print("Enter valid phone number. Example: 9098989765")
            number = input("Enter your number ")
        # appending the data
        address_json.append({
            "Name": name,
            "address": address,
            "city": city,
            "zipcode": zip_code,
            "state": state,
            "Number": number
            })
        final_address_dict['address'] = address_json
        final_address_dict = json.dumps(final_address_dict)
        with open('addressbook.json', 'w') as f:
            f.write(final_address_dict) # writing in json file with json writer
            logging.info(f"contact added successfully {address_json}")
            print("Contact added successfully")
    
        return final_address_dict
                
book = Addressbook()
book.main()
