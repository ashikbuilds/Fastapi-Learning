from pydantic import BaseModel
class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')
Patient_info = {'name':'Ashik','age':26}
Patient1 = Patient(**Patient_info)
insert_patient_data(Patient1)
update_patient_data(Patient1)