import json

from pydantic import BaseModel, Field, field_validator, ValidationError, EmailStr


class Address(BaseModel):
    city: str = Field(..., min_length=2, description='City name')
    street: str = Field(..., min_length=3, description='Street name')
    house_number: int = Field(..., gt=0, description='House number, positive integer number')


class User(BaseModel):
    is_employed: bool = Field(default=True, description='Whether user is employed')
    name: str = Field(..., pattern=r'^[a-zA-Z -]{2,50}$', description='User name')
    age: int = Field(..., ge=0, le=120, description='Age')
    email: EmailStr = Field(..., description='Email address')
    address: Address

    @field_validator('age')
    def validate_age_if_employee(cls, v, values, **kwargs):
        is_employed = values.data.get('is_employed')
        if is_employed and not (18 <= v <= 65):
            raise ValidationError('Age must be between 18 and 65')
        return v


def user_json_object(json_data: str):
    try:
        user = User.parse_raw(json_data)
        return user
    except ValidationError as e:
        return e.json()


json_input = """{
    "name": "John Doe",
    "age": 70,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""


user = user_json_object(json_input)
print(user)
