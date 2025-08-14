from pydantic import BaseModel


class Address(BaseModel):
    city: str
    street: str
    house_number: int


class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True
    address: Address

address = Address(city="New York", street="Green", house_number=1)

user = User(id=1, name="John Doe", age=30, address=address)

print(user)