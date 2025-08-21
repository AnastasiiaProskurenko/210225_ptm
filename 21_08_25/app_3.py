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
    user = session.query(User).get(1)
    if user:
        session.delete(user)
        session.commit()

        print('user deleted')

    print('-' * 20)
    users = session.query(User).all()
    print(*users, sep='\n')
