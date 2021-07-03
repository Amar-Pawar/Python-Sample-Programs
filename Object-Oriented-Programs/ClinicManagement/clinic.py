'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-1
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-2
@Title : Clinic Management
/**********************************************************************************
'''
import json
import re
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
            self.get_patient_data(patient_data)
        if choice == 3:
            self.book_appointment(doctor_data, patient_data)

        print("Do you want to try again? 1.Yes  2.No")
        choice = int(input())
        if choice == 1:
            self.main()
        else:
            return

    def get_doctor_data(self, doctor_data):
        """
        Description:
            This function gives the information about the doctors based on input provided by user as
            name, specialization, availability.
        Parameters:
            It takes doctor_data as parameter where we have loaded json file
        Return:
            It returns list of attributes of doctor
        """
        data_input = input("Enter details to search doctor by name, specialization, qualification: ")
        doctor_array = []
        for doctor in doctor_data['doctor_data']:
            if data_input in doctor.values():
                name = doctor['name']
                id = doctor['id']
                specialization = doctor['specialization']
                availability = doctor['availability']
                doctor_detail = {
                    "name": name,
                    "id": id,
                    "availability": availability,
                    "specialization": specialization
                }
                print(f"Id: {id} \nName: {name} \nSpecialization: {specialization} \nAvailability: {availability}")
                logger.info(f"Name: {name} \nSpecialization: {specialization} \nAvailability: {availability}")
                doctor_array.append(doctor_detail)
        return doctor_array

    def get_patient_data(self, patient_data):
        """
        Description:
            This function gives the information about the patient based on input provided by user as
            name, number, id.
        Parameters:
            It takes patient_data as parameter where we have loaded json file
        """
        data_input = input("Enter details to search patient: ")
        for patient in patient_data['patient_data']:
            if data_input in patient.values():
                name = patient['name']
                number = patient['number']
                print(f"Name: {name} \nNumber: {number}")
                logger.info(f"Name: {name} \nNumber: {number}")
        return

    def book_appointment(self,doctor_data, patient_data):
        """
        Description:
            This function is to book appointment with doctor by serching doctor by its attributes.
        Parameters:
            It takes doctor_data, patient_data as parameter where we have loaded json file
        """
        # check fot attribute is present or not
        doctor_array = self.get_doctor_data(doctor_data)
        if not doctor_array:
            print("No doctor present")
            self.book_appointment(doctor_data, patient_data)
        # asking user to select doctor based on id
        get_doctor = input("Enter doctor id you want book appointment with: ")
        pattern = re.compile("^[0-9]{1,}$") # reagex to validate input id
        if re.match(pattern,get_doctor):
            pass
        else:
            print("Enter proper doctors's id")
            self.book_appointment(doctor_data, patient_data)

        # condition to check if doctorwith given id is present or not
        flag_doctor = False
        for doctor in doctor_data['doctor_data']:
            if int(get_doctor) == doctor['id']:
                flag_doctor = True
        if not flag_doctor:
            print("No doctor found with such id")
            self.book_appointment(doctor_data, patient_data)
        # input from patient to enter its detail
        # validating name
        
        pattern = re.compile("^[A-Za-z]{3,}$")
        name = input("Enter your name: ")
        if re.match(pattern,name):
            pass
        else:
            print("Name should contain only letters ans min 3 characters Example: Amar")
            name = input("Enter your name: ")
        # validating numberaa
        
        pattern = re.compile("^[7-9]{1}[0-9]{9}$")
        number = input("Enter your number: ")
        if re.match(pattern,number):
            pass
        else:
            print("Enter valid phone number. Example: 9098989765")
            number = input("Enter your number: ")
        id = 0
        for data in patient_data['patient_data']:
            id = data['id']
        patient_detail = {
            "id": id+1,
            "name": name,
            "number": number
        }
        # appending the patient data
        patient_data['patient_data'].append(patient_detail)
        # adding patient details to doctors patient list
        for doctor in doctor_data['doctor_data']:
            if int(get_doctor) == doctor['id']:
                doctor['total_patients'] += 1
                doctor['patients_list'].append(patient_detail)
        # wrinting to json file
        with open('patient.json', 'w') as patient_details:
            patient_details.write(json.dumps(patient_data))
        #writing to json file
        with open('doctor.json', 'w') as doctor_details:
            doctor_details.write(json.dumps(doctor_data))
        print("Appointment booked successfully!!")
        logger.info(f"Appointment booked for {patient_detail}")
        return

clinic_management = ClinicManagement()
clinic_management.main()