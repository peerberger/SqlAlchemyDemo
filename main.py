from UserRepository import UserRepository
from db_cofig import local_session

repo = UserRepository(local_session)

users = repo.get_all()
print(users)
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
