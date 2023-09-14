#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Review, Restaurant

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restraurants.db')
    session = sessionmaker()(bind=engine)

    import ipdb; ipdb.set_trace()