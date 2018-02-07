"""Setup inicial do DB

Revision ID: c4a9d98a66b5
Revises: 9d19fcc6fdf0
Create Date: 2017-05-05 12:03:35.869039

"""

from alembic import op, context
from datetime import datetime

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c4a9d98a66b5'
down_revision = '9d19fcc6fdf0'


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    op.create_table('bank_receive',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('name', sa.String(length=256), nullable=False))

    op.create_table('bank',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.Column('payment_method', sa.Enum('Débito', 'Cheque', 'Consignado',
                                                        'Cartão de Crédito', 'Carnê'), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name'))

    op.create_table('uf',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.Column('initials', sa.String(length=256), nullable=True))

    op.create_table('customer',
                    sa.Column('id', sa.Integer, nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('name', sa.String(length=512), nullable=False),
                    sa.Column('document', sa.String(length=64), nullable=False),
                    sa.Column('city', sa.String(length=512), nullable=False),
                    sa.Column('email', sa.String(length=512), nullable=False),
                    sa.Column('uf_id', sa.Integer, nullable=True),
                    sa.ForeignKeyConstraint(['uf_id'], ['uf.id'], name='fk_customer_uf'),
                    sa.Column('bank_receive_id', sa.Integer, nullable=True),
                    sa.ForeignKeyConstraint(['bank_receive_id'], ['bank_receive.id'], name='fk_customer_bank_receive'),
                    sa.Column('created_at', sa.DateTime, nullable=False),
                    sa.Column('updated_at', sa.DateTime, nullable=True),
                    )

    op.create_table('phone',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('number', sa.String(length=64), nullable=True),
                    sa.Column('customer_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name='fk_phone_customer'),
                    sa.Column('type', sa.Enum('Celular', 'Fixo', 'Whats', 'Comercial'), nullable=True),
                    sa.Column('created_at', sa.DateTime, nullable=False),
                    sa.Column('updated_at', sa.DateTime, nullable=True))

    op.create_table('user',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('name', sa.String(length=64), nullable=True),
                    sa.Column('email', sa.String(length=64), nullable=True),
                    sa.Column('password', sa.String(length=64), nullable=True),
                    sa.Column('type', sa.Enum('Admin', 'Operator'), nullable=True),
                    sa.Column('created_at', sa.DateTime, nullable=False),
                    sa.Column('updated_at', sa.DateTime, nullable=True))

    op.create_table('contract',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    # TODO talvez migrar o date_contract para created_at
                    sa.Column('date_contract',sa.DateTime, nullable=False),
                    sa.Column('description', sa.String(length=512), nullable=True),
                    sa.Column('value', sa.DECIMAL(), nullable=True),
                    sa.Column('installments_count', sa.Integer, nullable=True),
                    sa.Column('status', sa.Enum('Análise', 'Aprovado', 'Efetivado', 'Pendente',
                              'Cancelado', 'Reprovado'), nullable=True),
                    sa.Column('method_contact', sa.Enum('Email', 'Balcao', 'Operador', 'Google Docs'), nullable=True),
                    sa.Column('bank_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['bank_id'], ['bank.id'], name='fk_contract_bank'),
                    sa.Column('customer_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name='fk_contract_customer'),
                    sa.Column('user_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_contract_user'),
                    sa.Column('created_at', sa.DateTime, nullable=False),
                    sa.Column('updated_at', sa.DateTime, nullable=True))



def schema_downgrades():
    op.drop_table('phone')
    op.drop_table('contract')
    op.drop_table('customer')
    op.drop_table('bank')
    op.drop_table('bank_receive')
    op.drop_table('uf')
    op.drop_table('user')


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass


def add_dates_insert(inserts):
    for insert in inserts:
        insert['created_at'] = datetime.utcnow()
        insert['updated_at'] = datetime.utcnow()
