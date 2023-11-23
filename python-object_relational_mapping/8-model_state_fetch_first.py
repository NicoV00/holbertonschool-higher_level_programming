#!/usr/bin/python3
"""Task 8"""
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(("mysql+mysqldb://{}:{}@localhost:3306/{}"
                            .format(argv[1], argv[2], argv[3])))
    
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).first()
    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
