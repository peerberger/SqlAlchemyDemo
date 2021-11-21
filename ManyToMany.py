from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db_cofig import Base


# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many

association_table = Table('teachers_students', Base.metadata,
    Column('teacher_id', ForeignKey('teachers.id'), primary_key=True),
    Column('student_id', ForeignKey('students.id'), primary_key=True)
)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    students = relationship('Student', secondary=association_table, backref='teachers')

    def __repr__(self):
        return f'<Order id={self.id} desc={self.name}>'


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)

    def __repr__(self):
        return f'<Order id={self.id} desc={self.name}>'
