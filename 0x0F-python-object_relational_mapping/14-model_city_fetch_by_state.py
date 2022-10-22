#!/usr/bin/python3
"""Lists all states via SQLAlchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for city in session.query(City).order_by(City.id).all():
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(
                    state.name,
                    city.id, city.name))

    session.commit()
    session.close()
