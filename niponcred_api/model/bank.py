from niponcred_api import db
from enum import Enum


class PaymentMethod(Enum):
    """
    Indica o metodo de pagamento.
    """

    Debito = 'Débito'
    Cheque = 'Cheque'
    Consignado = 'Consignado'
    Carne = 'Carnê'
    CreditCard = 'Cartão de Crédito'


class Bank(db.Model):

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    payment_method = db.Column(db.Enum(*[e.value for e in PaymentMethod]), nullable=False)

    def __repr__(self):
        return "%s.%s(id=%r)" % (self.__class__.__module__, self.__class__.__name__, self.id)

    def __str__(self):
        return "%s" % self.id or 'new object'

