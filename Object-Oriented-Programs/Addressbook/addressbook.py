'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-30
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-02
@Title : Addressbook System
/**********************************************************************************
'''

import json
import logging
import re
from logging_handler import logger

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

        print("Enter 1. To add contact 2.To delete contact 3.To update contact 4.To read contacts")
        
        choice = int(input("Enter your choice: "))
        try:
            with open('addressbook.json', 'r') as f:
                address_dict = json.load(f)
        except Exception as e:
            print("File not found")
            return

        if choice==1:
            self.add_contact(address_dict)

        elif choice == 2:
            self.delete_contact(address_dict)

        elif choice == 3:
            self.update_contact(address_dict)
        
        elif choice == 4:
            self.read_data()

        else:
            print("Invalid choice!! Please enter correct input")
            self.main()

        print("Do you want to try again? 1.Yes  2.No")
        choice = int(input())
        if choice == 1:
            self.main()
        else:
            return

    def read_data(self):
        f = open('addressbook.json',)
        data = json.load(f)
        for i in data['address']:
            print(i)
        
  
        # Closing file
        f.close()
                
    # function to update contact 
    def update_contact(self, address_json):
        """
        Description:
            This function is to delete contact from addressbook. It asks user to enter
            name and contact to delete the contact.
        Parameters:
            It takes address_json as parameter where we have loaded json file
        Return:
            It return addressbook dictionary
        """
        address_data = address_json['address']
        name = input("Enter name of contact to update ")
        number = input("Enter number of contact to update ")
        field_names = input("Enter which field/s to be updated - 1.Address 2.Contact Number 3.zip Code 4.City 5.state ")
        choice_id = field_names.split(",") # 1,3,4 ==> [1,3,4]
        choice_field_dict = {
            "1":"address",
            "2":"Number",
            "3":"zipcode",
            "4":"city",
            "5":"state"
        }
        with open("addressbook.json", 'w') as f:
            for data in address_data:
                if data['Name'] == name and data['Number'] == number:
                    for choice in choice_id:
                        try:
                            field_name = choice_field_dict[choice]
                        except Exception as e:
                            print("Please enter valid input")
                            self.update_contact(address_json)
                        input_value = input(f"Enter {choice_field_dict[choice]} ")
                        data[choice_field_dict[choice]] = input_value
                else:
                    print("Contact with given name not found!! Enter correct name")
                    self.update_contact(address_json)

            logger.info(address_json)
            address_json = json.dumps(address_json)
            f.write(address_json)
            logger.info(f"Contact updated sucessfully {address_json}")
    
        return address_json

    # function to delete contact
    def delete_contact(self, address_json):
        """
        Description:
            This function is to delete contact from addressbook. It asks user to enter
            name and contact to delete the contact.
        Parameters:
            It takes address_json as parameter where we have loaded json file
        Return:
            It return addressbook dictionary
        """
        address_data = address_json['address']
        name = input("Enter name of contact to delete ")
        number = input("Enter number of contact to update ")

        for data in address_data:
            if data['Name'] == name and data['Number'] == number:
                index = address_data.index(data)
                address_data.pop(index)
                logger.info(f"Contact deleted successfully {name}")
            else:
                print("Contact not found!! Please enter contact present in addressbook")
                self.delete_contact(address_json)

                with open("addressbook.json", 'w') as f:
                    address_json = json.dumps(address_json)
                    f.write(address_json)
    
        return address_data


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
            logger.info(f"contact added successfully {address_json}")
            print("Contact added successfully")
    
        return final_address_dict
                
book = Addressbook()
book.main()
