from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

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


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String)
    user = relationship("User", back_populates="addresses")

User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

# Создание её в базе данных и заполнение данными
Base.metadata.create_all(bind=engine)


with Session() as session:
    session.add_all([
        Address(user_id=3, description='New York'),
        Address(user_id=2, description='London'),
        Address(user_id=4, description='Berlin')
    ])
    session.commit()


# Присоединение таблицы адресов к таблице пользователей с помощью Inner Join
users = (session
         .query(User)
         .join(Address)
        )
# Проверка выборки
for user in users.all():
    print(user.id, user.name, user.age)
    for address in user.addresses:
        print("Address:", address.id, address.description)





from sqlalchemy.orm import aliased

address_alias1 = aliased(Address)
address_alias2 = aliased(Address)

users = (session
         .query(address_alias1.user_id, address_alias2.user_id)
         .join(address_alias2, address_alias1.description == address_alias2.description)
         .filter(address_alias1.user_id != address_alias2.user_id)
         .all()
         )
print(users)
