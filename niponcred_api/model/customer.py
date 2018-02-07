from niponcred_api import db

from niponcred_api.model.bank_receive import BankReceive
from niponcred_api.model.uf import Uf

from sqlalchemy import event

from gorillaspy.business.model import ModelBase
from gorillaspy.business.model.hooks import input_audit_data_on_insert, input_audit_data_on_update


class Customer(ModelBase, db.Model):

    name = db.Column(db.String(256), nullable=False)
    document = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(256), nullable=True)
    email = db.Column(db.String(256), nullable=True)
    uf_id = db.Column(db.Integer, db.ForeignKey(Uf.id), nullable=False)
    bank_receive_id = db.Column(db.Integer, db.ForeignKey(BankReceive.id), nullable=False)

    uf = db.relationship('Uf', foreign_keys=[uf_id])
    bank_receive = db.relationship('BankReceive', foreign_keys=[bank_receive_id])

    phones = db.relationship("Phone", back_populates="customer", cascade="all, delete-orphan", lazy='joined')

event.listen(Customer, 'before_insert', input_audit_data_on_insert)
event.listen(Customer, 'before_update', input_audit_data_on_update)
