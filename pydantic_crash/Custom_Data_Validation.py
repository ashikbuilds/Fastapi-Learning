from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length=5)
    age: int = Field(gt = 0, lt = 120)
    weight: float = Field(gt = 0, lt = 100)
    married: bool
    allergies: Optional[List[str]]=None
    contact_details: Dict[str, str]
    linkedin_url: AnyUrl

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.linkedin_url)
    print(patient.weight)
    print("Updated")

patient_info = {
    "name": "Ashik",
    "age": 26,
    "weight": 55.4,
    "married": True,
    "linkedin_url":"http://linekdin.com/1322",
    "contact_details": {
        "email": "mdashikurrahman2418@gmail.com",
        "phone": "01586357555"
    }
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)