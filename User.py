from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db_cofig import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f'<User id={self.id} username={self.username}>'
