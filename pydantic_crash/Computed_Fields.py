from typing import Optional, List, Dict
from pydantic import BaseModel, AnyUrl, Field, field_validator,model_validator, computed_field


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0, lt=100)
    height: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    linkedin_url: AnyUrl

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('BMI',patient.calculate_bmi)
    print("Inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.contact_details["email"])
    print(patient.contact_details["phone"])
    print("Updated")


patient_info = {
    "name": "Ashik",
    "age": 65,
    "weight": 55.4,
    "married": True,
    "height": 1.72,
    "linkedin_url": "https://linkedin.com/in/ashik",
    "contact_details": {
        "email": "mdashikurrahman2418@bubt.com",
        "phone": "01586357555",
        "emergency": "01744933469"
    }
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)