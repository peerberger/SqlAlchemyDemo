from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, backref
from db_cofig import Base


class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship("Car", backref=backref("driver", uselist=False))

    def __repr__(self):
        return f'<Driver id={self.id} desc={self.name}>'


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make_year = Column(DateTime(), nullable=False)

    def __repr__(self):
        return f'<Car id={self.id} desc={self.make_year}>'
