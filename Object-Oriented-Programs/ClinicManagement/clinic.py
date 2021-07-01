import json

class ClinicManagement:
    def __init__(self):
        print("Welcome to Clinic Management")

    def main():
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
            pass
        if choice == 2:
            pass
        if choice == 3:
            pass

clinic_management = ClinicManagement
clinic_management.main()