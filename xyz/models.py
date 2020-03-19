from datetime import datetime
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Ser
from flask_login import UserMixin
from xyz import _D, _L

@_L.user_loader
def uLoad(u_id):
    return Guy.query.get(int(u_id))
#
#
#
# Guy class
class Guy(_D.Model, UserMixin):
    id = _D.Column(
        _D.Integer,
        primary_key=True
    )
    fname = _D.Column(
        _D.String(20),
        nullable=False
    )
    lname = _D.Column(
        _D.String(20),
        nullable=False
    )
    email = _D.Column(
        _D.String(120),
        unique=True,
        nullable=False
    )
    num = _D.Column(
        _D.Integer,
        unique=True,
        default=7322958200
    )
    img = _D.Column(
        _D.String(20),
        nullable=False,
        default='pic.jpg'
    )
    pw = _D.Column(
        _D.String(60),
        nullable=False
    )
    schedule = _D.relationship(
        'Work',
        backref='employee',
        lazy=True
    )

    def resetToken(self, expires_sec=1800):
        s = Ser(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'u_id': self.id}).decode('utf=8')

    @staticmethod
    def verifyReset(token):
        s = Ser(current_app.config['SECRET_KEY'])
        try:
            u_id = s.loads(token)['u_id']
        except:
            return None
        return Guy.query.get(u_id)

    def __repr__(self):
        return f"Guy('{self.fname}', '{self.fname}', '{self.email}', '{self.num}', '{self.img}')"
#
#
#
# Calendar Class
class Calendar(_D.Model):
    id = _D.Column(
        _D.Integer,
        primary_key=True
    )
    weekday = _D.Column(
        _D.String(5),
        nullable=False
    )
    day = _D.Column(
        _D.Integer,
        nullable=False
    )
    month = _D.Column(
        _D.String(3),
        nullable=False
    )
    year = _D.Column(
        _D.Integer,
        nullable=False
    )

    def __repr__(self):
        return f"Calendar('{self.weekday}', '{self.day}', '{self.month}', '{self.year}')"
#
#
#
# Schedule class
class Schedule(_D.Model):
    id = _D.Column(
        _D.Integer,
        primary_key=True
    )
