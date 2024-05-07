from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///club_membership.db')  # Adjust for your database
session_factory = sessionmaker(bind=engine, expire_on_commit=True)
Session = scoped_session(session_factory)

class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    unpaid_classes = Column(Integer, default=0)
    attendance = Column(Integer, default=0)
    payments = relationship('Payment', back_populates='member')

class Payment(Base):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    amount = Column(Float)
    date = Column(Date)
    member = relationship('Member', back_populates='payments')

class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Float)
    date = Column(Date)

