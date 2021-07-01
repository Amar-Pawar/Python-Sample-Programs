'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-1
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-1
@Title : Clinic Management
/**********************************************************************************
'''
import json
from logging_handler import logger

class ClinicManagement():
    # creating a consteuctor
    def __init__(self):
        print("Welcome to Clinic Management")

    def main(self):
        """
        Description:
            This is main function it will call other methods to execute.
            It will ask user to make choice and accordingly call methods
        """
        print("Select Operation 1.Search Doctor 2.Search Patient 3.Book Appointment: ")
        choice = int(input())
        try:
            with open("doctor.json", 'r') as doctor_details:
                doctor_data = json.load(doctor_details)
            with open("patient.json", 'r') as patient_details:
                patient_data = json.load(patient_details)
        except Exception as e:
            print(f"Error while reading file {e}")
            return

        if choice == 1:
            self.get_doctor_data(doctor_data)
        if choice == 2:
            pass
        if choice == 3:
            pass

    def get_doctor_data(self, doctor_data):
        """
        Description:
            This function gives the information about the doctors based on input provided by user as
            name, specialization, availability.
        Parameters:
            It takes doctor_data as parameter where we have loaded json file
        """
        data_input = input("Enter details to search doctor: ")
        for doctor in doctor_data['doctor_data']:
            if data_input in doctor.values():
                name = doctor['name']
                specialization = doctor['specialization']
                availability = doctor['availability']
                print(f"Name: {name} \nSpecialization: {specialization} \nAvailability: {availability}")
                logger.info(f"Name: {name} \nSpecialization: {specialization} \nAvailability: {availability}")
        return

clinic_management = ClinicManagement()
clinic_management.main()