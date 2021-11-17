from UserRepository import UserRepository
from db_cofig import local_session, create_all_entities

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
# result = local_session.execute(text('SELECT * FROM sp_get_all()'))
# # users = [User(user[0], user[1], user[2], user[3]) for user in result]
# users = [User(user._mapping['id'], user._mapping['username'], user._mapping['email'], user._mapping['date_created'])
#          for user in result]
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
# user = repo.get_by_id(2)
# print()
