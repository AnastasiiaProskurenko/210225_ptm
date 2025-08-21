from sqlalchemy import func
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
    total_ages = session.query(User.name, func.sum(User.age), func.avg(User.age)).group_by(User.name)
    res = total_ages.all()

    for item in res:
        print(*item)

    res = session.query(func.count(User.id)).first()
    res, *_ = res
    print(res)

    res = session.query(func.count(User.id)).scalar()
    print(res)

    res = session.query(User.name, User.age).filter(User.id == 2)
    print(res)

    # Присвоение алиаса выражению подсчета количества пользователей в каждой возрастной группе
    age_groups = session.query(User.age,
                               func.count(User.id)).group_by(User.age)


    age_groups = session.query(User.age,
                               func.count(User.id).label('total_users')).group_by(User.age)

    print()



    # # Тот же запрос, но с обращением к таблице через алиас
    # age_groups = session.query(user_alias.age,
    #                            func.count(user_alias.id).label('total_users')).group_by(user_alias.age).all()
    # # Теперь можно обращаться к присвоенному имени
    # for group in age_groups:
    #     print(group.age, group.total_users)