from sqlalchemy import func, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import (Column, Integer, String, 
    Float, ForeignKey, DateTime, Table, MetaData)
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine('sqlite:///restraurants.db')

Base = declarative_base(metadata=metadata)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)

    def __repr__(self):
        return f"Restaurant ID: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Price: {self.price}"
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    def __repr__(self):
        return f"Restaurant ID: {self.id}, " \
            + f"First Name: {self.first_name}, " \
            + f"Last Name: {self.last_name}"
