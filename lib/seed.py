from faker import Faker
import random 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Customer

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
    restaurants =[]
    for i in range(14):
        restaurant = Restaurant(
            name = random.choice(restaurant_stores),
            price =random.randint(3000, 10000)
        )
    session.add(restaurant)
    session.commit()
    restaurants.append(restaurant)
    print(restaurants)

    #generating random data for the Customer Table
    customers = []
    for i in range(30):
        customer = Customer(
            first_name = fake.first_name(), 
            last_name = fake.last_name(),
        )
    session.add(customer)
    session.commit()
    customers.append(customer)