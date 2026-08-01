from typing import Optional, List, Dict
from pydantic import BaseModel, AnyUrl, Field, field_validator,model_validator


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0, lt=100)
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    linkedin_url: AnyUrl

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator("contact_details")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["bubt.com", "edu.bd"]

        email = value.get("email")

        if email is None:
            raise ValueError("Email is required")

        domain_name = email.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value

    @field_validator('age',mode = 'before')
    @classmethod
    def validate_age(cls, value):
        if 0< value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
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
    print(patient.contact_details["email"])
    print(patient.contact_details["phone"])
    print("Updated")


patient_info = {
    "name": "Ashik",
    "age": 65,
    "weight": 55.4,
    "married": True,
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