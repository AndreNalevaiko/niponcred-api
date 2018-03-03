from niponcred_api import db
from niponcred_api.model import Contract, User
from gorillaspy.business.model import ModelBase

class AnnotationContract(db.Model, ModelBase):

    annotation = db.Column(db.String(512), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey(Contract.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    contract = db.relationship('Contract', foreign_keys=[contract_id])
    user = db.relationship('User', foreign_keys=[user_id])


    def __repr__(self):
        return "%s.%s(id=%r)" % (self.__class__.__module__, self.__class__.__name__, self.id)

    def __str__(self):
        return "%s" % self.id or 'new object'

