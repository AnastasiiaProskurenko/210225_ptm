from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    addresses = relationship("Address", back_populates="user", order_by="Address.id")

    def __str__(self):
        return f'{self.id=} {self.name=} {self.age=}'


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String)

    user = relationship("User", back_populates="addresses")

    def __str__(self):
        return f'{self.id=} {self.description=}'



with Session() as session:
    # users = session.query(User).options(joinedload(User.addresses))
    # for user in users.all():
    #     print(user.id, user.name, user.age)
    #     for address in user.addresses:
    #         print("Address:", address.id, address.description)


    rows = (session
             .query(User, Address)
             .join(Address)
             )
    for user, addr in rows.all():
        print(user, addr)
