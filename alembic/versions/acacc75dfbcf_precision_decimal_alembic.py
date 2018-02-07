"""precision decimal alembic

Revision ID: acacc75dfbcf
Revises: 74b5188ab2a2
Create Date: 2018-02-07 00:00:05.106110

"""

from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acacc75dfbcf'
down_revision = '74b5188ab2a2'


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    contract_value_alter = """
    ALTER TABLE contract 
        MODIFY contract.value DECIMAL(17, 4) NULL
    ;
    """

    op.execute(contract_value_alter)


def schema_downgrades():
    contract_value_alter = """
    ALTER TABLE contract 
        MODIFY value DECIMAL() NULL,
    ;
    """


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
