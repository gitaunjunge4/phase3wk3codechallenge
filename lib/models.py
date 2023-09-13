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

class 

