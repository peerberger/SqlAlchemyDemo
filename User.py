from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db_cofig import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow())
    orders = relationship("Order")

    def __init__(self, id, username, email, date_created):
        self.id = id
        self.username = username
        self.email = email
        self.date_created = date_created

    def __repr__(self):
        return f'<User id={self.id} username={self.username}>'
