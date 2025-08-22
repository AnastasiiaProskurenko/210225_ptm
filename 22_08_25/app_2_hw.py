from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from faker import Faker
import random

engine = create_engine('sqlite:///hw_test.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)

faker = Faker("ru_RU")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Numeric(10,2))
    in_stock = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='products')

    def __str__(self):
        return f'{self.id=}; {self.name=}; {self.price=}'


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))

    products = relationship('Product', back_populates='category')

    def __str__(self):
        return f'{self.id=}; {self.name=}; {self.description=}'


Base.metadata.create_all(engine)


categories = [Category(name=faker.company(), description=faker.sentence(nb_words=3)) for _ in range(5)]
print(*categories, sep='\n ')

session = Session()
session.add_all(categories)
session.commit()

for category in categories:
    for _ in range(random.randint(4, 10)):
        product = Product(
            name=faker.word().capitalize(),
            price=random.randint(1, 100),
            in_stock=random.choice([True, False]),
            category=category,
        )
        session.add(product)
session.commit()

















