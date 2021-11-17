from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

connection_string = 'postgresql+psycopg2://postgres:admin@localhost/sqlalchemy_test'

Base = declarative_base()

engine = create_engine(connection_string, echo=True)


def create_all_entities():
    Base.metadata.create_all(engine)


Session = sessionmaker()

# https://stackoverflow.com/questions/12223335/sqlalchemy-creating-vs-reusing-a-session
local_session = Session(bind=engine)
