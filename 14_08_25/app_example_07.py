from pydantic import BaseModel, field_validator, ValidationError, EmailStr

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

    @field_validator('email')
    def check_email_domain(cls, value):
        allowed_domains = ['example.com', 'test.com']
        email_domain = value.split('@')[-1]
        if email_domain not in allowed_domains:
            raise ValueError(f"Email must be from one of the following domains: {', '.join(allowed_domains)}")
        return value


# Пример создания пользователя
try:
    # Этот email проходит валидацию
    user_valid = User(name="Alice", age=30, email="alice@example.com")
    print(f"Valid user: {user_valid}")
    # Этот email вызовет ошибку валидации
    user_invalid = User(name="Bob", age=25, email="bob@gmail.com")
except ValidationError as e:
    print(e)