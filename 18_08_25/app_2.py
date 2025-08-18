from sqlalchemy import Column, Integer, String, ForeignKey, Numeric

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    owner = Column(String(50), nullable=False)
    balance = Column(Numeric(10, 2), default=0.00)


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    amount = Column(Numeric(10, 2))
    account = relationship("Account", back_populates="transactions")




