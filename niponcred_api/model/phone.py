from enum import Enum

from niponcred_api import db
from .customer import Customer

from sqlalchemy import event

from gorillaspy.business.model import ModelBase
from gorillaspy.business.model.hooks import input_audit_data_on_insert, input_audit_data_on_update


class PhoneType(Enum):
    """
    Indica o tipo do telefone.
    """

    Celular = 'Celular'
    Fixo = 'Fixo'
    Whats = 'Whats'
    Comercial = 'Comercial'

class Phone(ModelBase, db.Model):

    number = db.Column(db.String(256), nullable=False)
    type = db.Column(db.Enum(*[e.value for e in PhoneType]), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id), nullable=False)

    customer = db.relationship('Customer', back_populates='phones')

event.listen(Phone, 'before_insert', input_audit_data_on_insert)
event.listen(Phone, 'before_update', input_audit_data_on_update)