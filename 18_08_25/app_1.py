from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('sqlite:///example.db')

metadata = MetaData()
metadata.reflect(bind=engine)
Base = automap_base(metadata=metadata)
Base.prepare()


# print(metadata.tables)


User = Base.classes.users


user1 = User(name="Tom", age=20)
print(user1)