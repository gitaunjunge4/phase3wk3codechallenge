from sqlalchemy import func, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (Column, Integer, String, 
    Float, ForeignKey, DateTime, Table, MetaData)
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)


Base = declarative_base(metadata=metadata)

restaurant_customer = Table(
    'restaurant_customer', 
    Base.metadata, 
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)

    reviews = relationship('Review', backref=backref('restaurants'))
    customers = relationship('Customer  ', secondary=restaurant_customer, back_populates='customers')

    def __repr__(self):
        return f"Restaurant ID: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Price: {self.price}"
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    reviews = relationship("Review", backref=backref('customer'))
    restaurants = relationship('Restaurant', secondary=restaurant_customer, back_populates='restaurants')

    def __repr__(self):
        return f"Restaurant ID: {self.id}, " \
            + f"First Name: {self.first_name}, " \
            + f"Last Name: {self.last_name}."
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer(), nullable=False)

    customer_id = Column(Integer(), ForeignKey("customers.id"))
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))

    def __repr__(self):
        return f"ReviewID: {self.id}, " \
            + f"Star Rating: {self.star_rating}, " \
            + f"CustomerID: {self.customer_id}, " \
            + f"RestaurantID: {self.restaurant_id}"