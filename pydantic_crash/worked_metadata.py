from typing import Annotated, List, Dict, Optional
from pydantic import BaseModel, AnyUrl, Field


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give the name of the patient in less than 50 characters",
            examples=["Ashik", "Rahman"],
        ),
    ]

    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, lt=100, strict=True)]
    married: Annotated[bool,Field(default=None,
                                  description='Is the Patient married or not')]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
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
    "linkedin_url": "https://linkedin.com/in/ashik",
    "contact_details": {
        "email": "mdashikurrahman2418@gmail.com",
        "phone": "01586357555",
    },
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)