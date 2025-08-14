from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        str_min_length = 2
        str_strip_whitespace = True
        json_encoders = {
            datetime: lambda dt: dt.strftime('%Y-%m-%d %H:%M')
        }


user = User(first_name='    ', last_name='Doe', email='tom@example.com', created_at=datetime.now(), updated_at=datetime.now(),)


