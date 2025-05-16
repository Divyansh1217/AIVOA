from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,declarative_base

Base= declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    