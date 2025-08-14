from pydantic import BaseModel, EmailStr, field_validator, ValidationError


class User(BaseModel):
    name: str
    email: EmailStr

    @field_validator('name')
    def name_validate(cls, value: str):
        if not value.isalpha():
            raise ValueError('Name must be alphanumeric')
        return value

    @field_validator('email')
    def email_validate(cls, value: str):
        if not value.endswith('.com'):
            raise ValueError('Email must end with .com')
        return value


try:
    user_1 = User(name='Tom', email='example@example.com')
except ValidationError as e:
    print(e)