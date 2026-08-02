from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dic = {'city': 'Mirpur', 'state':'Dhaka','pin':'1216'}
address1 = Address(**address_dic)

patient_dict = {'name':'Ashik','gender':'male','age':26,'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

#seialization

temp = patient1.model_dump()
print(temp)
print(type(temp))


temp = patient1.model_dump(include = ['name','gender'])
print(temp)
print(type(temp))

temp = patient1.model_dump_json(exclude = {'address':['state']})
print(temp)
print(type(temp))