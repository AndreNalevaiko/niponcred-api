from enum import  Enum

from niponcred_api import db

from niponcred_api.model import  Bank, Customer

from sqlalchemy import event

from gorillaspy.business.model import ModelBase
from gorillaspy.business.model.hooks import input_audit_data_on_insert, input_audit_data_on_update


class Status(Enum):
    """
    Indica o status do contrato.
    """

    Analise = 'Análise'
    Aprovado = 'Aprovado'
    Efetivado = 'Efetivado'
    Pendente = 'Pendente'
    Cancelado = 'Cancelado'
    Reprovado = 'Reprovado'


class MethodContact(Enum):
    """
    Indica o meio de contato.
    """

    Email = 'Email'
    Balcao = 'Balcao'
    Operador = 'Operador'
    GoogleDocs = 'Google Docs'

class Contract(ModelBase, db.Model):

    date_contract = db.Column(db.DateTime(), nullable=False)
    value = db.Column(db.DECIMAL(asdecimal=False, precision=17, scale=2), nullable=False)
    installments_count = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Enum(*[e.value for e in Status]), nullable=False)
    method_contact = db.Column(db.Enum(*[e.value for e in MethodContact]), nullable=False)
    changed_by = db.Column(db.String(64), nullable=True)

    bank_id = db.Column(db.Integer, db.ForeignKey(Bank.id), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    bank = db.relationship('Bank', foreign_keys=[bank_id])
    customer = db.relationship('Customer', foreign_keys=[customer_id])
    # user = db.relationship('User', foreign_keys=[user_id])

event.listen(Contract, 'before_insert', input_audit_data_on_insert)
event.listen(Contract, 'before_update', input_audit_data_on_update)
