from datetime import date
from run import DB


class User(DB.Model):
    """ Basic user information """

    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(10))
    email = DB.Column(DB.String(80), unique=True, nullable=False)
    password_hash = DB.Column(DB.String(100))
    created_at = DB.Column(DB.DateTime, default=date.today())

    def __repr__(self):
        """ User representation when queried """

        return '< Username: {} and Email {}>'.format(self.username, self.email)
