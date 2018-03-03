from enum import Enum
from niponcred_api import db

from sqlalchemy import event

from gorillaspy.business.model import ModelBase
from gorillaspy.business.model.hooks import input_audit_data_on_insert, input_audit_data_on_update



class UserType(Enum):
    """
    Indica o tipo do usuário.
    """
    Admin = 'Admin'
    Operator = 'Operator'

class User(ModelBase, db.Model):

    name = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    type = db.Column(db.Enum(*[e.value for e in UserType]), nullable=True)


event.listen(User, 'before_insert', input_audit_data_on_insert)
event.listen(User, 'before_update', input_audit_data_on_update)