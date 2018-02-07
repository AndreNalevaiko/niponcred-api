from niponcred_api import db

from sqlalchemy import event

from gorillaspy.business.model.hooks import input_audit_data_on_insert, input_audit_data_on_update


class Uf(db.Model):

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    initials = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "%s.%s(id=%r)" % (self.__class__.__module__, self.__class__.__name__, self.id)

    def __str__(self):
        return "%s" % self.id or 'new object'

event.listen(Uf, 'before_insert', input_audit_data_on_insert)
event.listen(Uf, 'before_insert', input_audit_data_on_insert)
event.listen(Uf, 'before_insert', input_audit_data_on_insert)
event.listen(Uf, 'before_insert', input_audit_data_on_insert)
event.listen(Uf, 'before_update', input_audit_data_on_update)
