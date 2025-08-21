from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


Base.metadata.create_all(engine)
session = Session()

new_user = User(name="John", age=23)
session.add(new_user)

session.add_all(
    [
        User(name='Bob', age=22),
        User(name='David', age=27),
        User(name='Alice', age=30),
        User(name='Ann', age=17),
        User(name='Ann', age=27)
    ]
)
session.commit()


# with Session() as session:
#    ...