"""changed_by and alter column contract

Revision ID: 74b5188ab2a2
Revises: 0ce8e222ecec
Create Date: 2018-02-03 13:15:43.447025

"""

from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74b5188ab2a2'
down_revision = '0ce8e222ecec'


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    op.alter_column('contract', 'value', nullable=True, type_=sa.DECIMAL(precision=17, scale=2))
    op.add_column('contract', sa.Column('changed_by', sa.String(length=128)))


def schema_downgrades():
    op.alter_column('contract', 'value', nullable=True, type_=sa.DECIMAL(precision=17, scale=2))
    op.drop_column('contract', 'changed_by')


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
