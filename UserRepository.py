from sqlalchemy import asc, text
from User import User


class UserRepository:
    def __init__(self, local_session):
        self.local_session = local_session

    def get_all(self):
        return self.local_session.query(User).all()

    def get_all_limit(self, limit_num):
        return self.local_session.query(User).limit(limit_num).all()

    # https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.order_by
    def get_all_order_by(self, column, direction=asc):
        return self.local_session.query(User).order_by(direction(column)).all()

        # the default directions is ascending
        # return self.local_session.query(User).order_by(column).all()

    # Session.get() is for filtering specifically by primary key
    # https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.get
    def get_by_id(self, id):
        return self.local_session.get(User, id)

    def get_by_username(self, username):
        return self.local_session.query(User).filter(User.username == username).first()

    def add(self, user):
        self.local_session.add(user)

        self.local_session.commit()

    def add_all(self, users):
        self.local_session.add_all(users)

        self.local_session.commit()

    # https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.update
    def update(self, id, data):
        # data = {User.username: 'baba'}
        # data = {'username': 'baba'}
        rows_affected = self.local_session.query(User).filter(User.id == id)\
            .update(data, synchronize_session=False)

        self.local_session.commit()

        return rows_affected

        # another way to manually update:
        # user_to_update = self.local_session.query(User).filter(User.id == 2).first()
        #
        # user_to_update.username = 'baba'
        #
        # self.local_session.commit()

    # https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.delete
    def delete(self, id):
        rows_affected = self.local_session.query(User).filter(User.id == id)\
            .delete(synchronize_session=False)

        self.local_session.commit()

        return rows_affected

        # another way to manually delete:
        # user_to_delete = local_session.query(User).filter(User.id == 14).first()
        #
        # local_session.delete(user_to_delete)
        #
        # local_session.commit()
