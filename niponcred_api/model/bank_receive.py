from niponcred_api import db


class BankReceive(db.Model):

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "%s.%s(id=%r)" % (self.__class__.__module__, self.__class__.__name__, self.id)

    def __str__(self):
        return "%s" % self.id or 'new object'

