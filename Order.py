from sqlalchemy import Column, Integer, ForeignKey, String

from db_cofig import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))

    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name
