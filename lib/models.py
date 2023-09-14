from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String, ForeignKey, Table, MetaData)
from sqlalchemy.ext.declarative import declarative_base
# from debug import session

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///restraurants.db')
session = sessionmaker()(bind=engine)

#association table
restaurant_customer = Table(
    'restaurant_customer', 
    Base.metadata, 
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)


#schema for restaurant table
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(Integer(), nullable=False)

    reviews = relationship('Review', back_populates=('restaurant'))
    customers = relationship(
        'Customer', 
        secondary=restaurant_customer, 
        back_populates='restaurants'
    )

    def __repr__(self):
        return f"Restaurant ID: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Price: {self.price}"
    
    #collection of all the reviews for the `Restaurant`
    def restaurant_reviews(self):
        return self.reviews
    
    #collection of all the customers who reviewed the `Restaurant`
    def restaurant_customer(self):
        return self.customers

    @classmethod
    def fanciest(cls):
        fancy = session.query(cls).order_by(cls.price.desc()).first()
        return print(fancy)
    
    def all_reviews(self):
        return {f"Review for {self.name} by {self.reviews.customer.full_name()}: {self.reviews.star_rating} stars." for review in self.restaurant_reviews()}


#schema for customers table   
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    # reviews = relationship("Review", backref=('customer'))
    restaurants = relationship(
        'Restaurant', 
        secondary=restaurant_customer,
        back_populates='customers'
    )

    def __repr__(self):
        return f"Customer ID: {self.id}, " \
            + f"First Name: {self.first_name}, " \
            + f"Last Name: {self.last_name}."
    
    #return a collection of all the reviews that the `Customer` has left
    def customer_review(self):
        return self.reviews
    
    #return a collection of all the restaurants that the `Customer` has reviewed
    def customer_restaurant(self):
        return self.restaurants
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        return session.query(Restaurant).join(Review).filter(Review.customer_id == self.id).order_by(Review.star_rating.desc()).first()

    def add_review(self, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
        customer_reviews = session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).all()
        for review in customer_reviews:
            session.delete(review)
        session.commit()


#schema for reviews table
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer(), nullable=False)

    customer_id = Column(Integer(), ForeignKey("customers.id"))
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))

    restaurant = relationship('Restaurant', back_populates='reviews')

    customer = relationship('Customer', backref='customers')

    def __repr__(self):
        return f"ReviewID: {self.id}, " \
            + f"Star Rating: {self.star_rating}, " \
            + f"CustomerID: {self.customer_id}, " \
            + f"RestaurantID: {self.restaurant_id}"
    
    #returns the Customer instance for this review
    def review_customer(self):
        return self.customer
    
    #return the `Restaurant` instance for this review
    def review_restaurant(self):
        return self.restaurant
    
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."