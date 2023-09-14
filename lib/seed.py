from faker import Faker
import random 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Customer, Review

if __name__ == '__main__':

    engine = create_engine('sqlite:///restraurants.db')
    session = sessionmaker()(bind=engine)

    session.query(Restaurant).delete()
    session.query(Customer).delete()

    fake = Faker()

    restaurant_stores = [
        "Jiko", "Red Ginger" , "Carnivore", "The View", "About Thyme", "The Harvest",
        "Galitos", "Chicken Inn", "Pizza Inn", "KFC", "Spur", "Java", "News Cafe", "Artcaffe", "Cjs"
    ]

    #generating random data for the Restaurant Table
    for i in range(14):
        restaurant = Restaurant(
            name = random.choice(restaurant_stores),
            price =random.randint(3000, 10000)
        )
    session.add(restaurant)
    session.commit()
    restaurants = [x.id for x in session.query(Restaurant)]
    print(restaurants)


    #generating random data for the Customer Table
    for i in range(30):
        customer = Customer(
            first_name = fake.first_name(), 
            last_name = fake.last_name(),)
    session.add(customer)
    session.commit()
    customers = [x.id for x in session.query(Customer)]
    print(customers)


    #generating random data for the Reviews Table
    reviews = []
    for i in range(20):
        review = Review(
            star_rating = random.randint(1, 5),
            customer_id = random.choice(customers),
            restaurant_id = random.choice(restaurants)
        )
        reviews.append(review)
    session.bulk_save_objects(reviews)
    session.commit()
    print(reviews)