from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]=None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Updated")

patient_info = {
    "name": "Ashik",
    "age": 26,
    "weight": 55.4,
    "married": True,
    
    "contact_details": {
        "email": "mdashikurrahman2418@gmail.com",
        "phone": "01586357555"
    }
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)