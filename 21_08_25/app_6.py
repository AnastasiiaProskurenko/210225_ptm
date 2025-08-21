from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __str__(self):
        return f'{self.id=} {self.name=} {self.age=}'


with Session() as session:
    # | = or, & = and, ~ - not

    users = session.query(User).filter(
        (User.name.like('J%')) |
        (User.age == 17)
    ).all()
    print(*users, sep='\n')
