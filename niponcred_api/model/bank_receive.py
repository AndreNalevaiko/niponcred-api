from niponcred_api import db

from sqlalchemy import event

from gorillaspy.business.model import ModelBase
from gorillaspy.business.model.hooks import input_audit_data_on_insert, input_audit_data_on_update


class BankReceive(ModelBase, db.Model):

    name = db.Column(db.String(256), nullable=False)

event.listen(BankReceive, 'before_insert', input_audit_data_on_insert)
event.listen(BankReceive, 'before_update', input_audit_data_on_update)
