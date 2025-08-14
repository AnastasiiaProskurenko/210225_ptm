from pydantic import BaseModel, EmailStr, ValidationError


class Address(BaseModel):
    city: str
    street: str
    house_number: int


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    address: Address


json_string = """{
    "name": "John Doe",
    "age": 22,
    "email": "john.doe@example.com",
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""


try:
    user = User.model_validate_json(json_string, strict=True)
    print(user)

    print(user.model_dump_json())
except ValidationError as e:
    print(e)