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