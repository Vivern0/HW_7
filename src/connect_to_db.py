'''
This module is used to connect to the database
and create a session object to interact with the database.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
