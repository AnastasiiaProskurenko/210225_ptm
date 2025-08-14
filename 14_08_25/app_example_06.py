from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(18, gt=18, description="GT 18")
    is_subscribed: bool = False
    is_active: bool = Field(default=True, description="Can use site")

try:
    user = User(name='Tom', age=10)

    print(user)

    print(user.model_dump_json())

    print(user.model_json_schema())

except Exception as e:
    print(e)