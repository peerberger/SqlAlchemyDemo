from datetime import datetime
from OneToOne import Driver, Car
from User import User
from Order import Order
from ManyToMany import Teacher, Student
from sqlalchemy import text
from UserRepository import UserRepository
from db_cofig import local_session, create_all_entities

# NOTE THAT IN ORDER TO RECOGNIZE NEW ENTITY CLASSES FOR CREATION
# YOU NEED TO IMPORT THEM SO PYTHON RUNS THEIR MODULES!
create_all_entities()
repo = UserRepository(local_session)

# users = repo.get_all()
# print(users)
#
#
# users = repo.get_all_limit(2)
# print(users)
#
#
# user = repo.get_by_id(2)
# print(user)
#
#
# user = repo.get_by_username('lala')
# print(user)
#
#
# repo.add(User(username='bob', email='bob@bob.com'))
# users = repo.get_all()
# print(users)
#
#
# users = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
# repo.add_all(users)
# users = repo.get_all()
# print(users)
#
#
# data = {User.username: 'baba'}
# # data = {'username': 'baba'}
# rows_affected = repo.update(2, data)
# users = repo.get_all()
# print(f'rows affected: {rows_affected}')
# print(users)
#
#
# rows_affected = repo.delete(14)
# users = repo.get_all()
# print(f'rows affected: {rows_affected}')
# print(users)
#
#
# column = User.username
# # column = 'username'
# users_asc = repo.get_all_order_by(column)
# users_desc = repo.get_all_order_by(column, desc)
# print(users_asc)
# print(users_desc)
#
#
# ---------- Plain SQL and Stored Procedures ----------
#
#
# result = local_session.execute(text('SELECT * FROM sp_get_all()'))
# users = [User(id=user[0], username=user[1], email=user[2], date_created=user[3]) for user in result]
# # users = [User(id=user._mapping['id'],
# #               username=user._mapping['username'],
# #               email=user._mapping['email'],
# #               date_created=user._mapping['date_created'])
# #          for user in result]
# print(users)
#
#
# count = local_session.execute(text('SELECT COUNT(id) FROM users')).scalar()
# print(count)
#
#
# https://docs.sqlalchemy.org/en/14/core/tutorial.html#specifying-bound-parameter-behaviors
# stmt = text('SELECT * FROM sp_get_all_between_ids(:x, :y)').bindparams(x=3, y=8)
# result = local_session.execute(stmt)
# users = [User(user[0], user[1], user[2], user[3]) for user in result]
# print(users)
#
#
# ---------- Relationships ----------
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
#
#
# orders = [Order(desc='soap', user_id=2), Order(desc='coacoa', user_id=2), Order(desc='sugar', user_id=2)]
# local_session.add_all(orders)
# local_session.commit()
# order = local_session.get(Order, 2)
# desc = order.desc
# user = order.user  # with backref
# print(desc)
# print(user)
#
#
# teacher = Teacher(
#     name='mr steve',
#     students=[
#         Student(name='nikki'),
#         Student(name='barbara')
# ])
# # local_session.add(teacher)
# local_session.commit()
#
#
# driver = Driver(
#     name='carl',
#     car=Car(
#         make_year=datetime(2020, 1, 1, 0, 0, 0)
#     )
# )
# local_session.add(driver)
# local_session.commit()
#
# car = local_session.get(Car, 1)
# print(car.driver)
#
#
# ---------- Join ----------
# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_joins.htm
#
#
# res1 = local_session.query(User, Student).filter(User.id == Student.id).all()
# print(res1)
