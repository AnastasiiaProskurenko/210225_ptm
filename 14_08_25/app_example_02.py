from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True

    def __str__(self):
        return self.name


user_1 = User(id=1, name='John', age=20, is_active=True)
print(user_1)

