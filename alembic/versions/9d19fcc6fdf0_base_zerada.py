"""Base zerada

Revision ID: 9d19fcc6fdf0
Revises: None
Create Date: 2017-05-05 12:04:06.684120

"""

from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d19fcc6fdf0'
down_revision = None


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    """schema upgrade migrations go here."""
    pass


def schema_downgrades():
    """schema downgrade migrations go here."""
    pass


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
