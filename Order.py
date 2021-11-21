from sqlalchemy import Column, Integer, ForeignKey, String
from db_cofig import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    desc = Column(String(25), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f'<Order id={self.id} desc={self.desc}>'
