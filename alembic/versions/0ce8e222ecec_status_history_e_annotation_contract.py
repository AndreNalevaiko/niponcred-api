"""status history e annotation contract

Revision ID: 0ce8e222ecec
Revises: c4a9d98a66b5
Create Date: 2018-01-31 23:06:26.956481

"""

from alembic import op, context
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0ce8e222ecec'
down_revision = 'c4a9d98a66b5'


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    op.create_table('annotation_contract',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('annotation', sa.String(length=512), nullable=True),
                    sa.Column('contract_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], name='fk_annotation_contract'),
                    sa.Column('user_id', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_annotation_user'),
                    sa.Column('created_at', sa.DateTime, nullable=False),
                    sa.Column('updated_at', sa.DateTime, nullable=True))

    op.create_table('contract_status_history',
                    sa.Column('id', sa.Integer(), nullable=False), sa.PrimaryKeyConstraint('id'),
                    sa.Column('status', sa.Enum('Análise', 'Aprovado', 'Efetivado', 'Pendente',
                                                'Cancelado', 'Reprovado'), nullable=False),
                    sa.Column('changed_by', sa.String(length=64), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime()),
                    sa.Column('contract_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], name='fk_contract_status_contract')
                    )

    op.execute("""insert into annotation_contract (annotation, contract_id, user_id, created_at)
                  SELECT description, id, user_id, NOW() FROM contract;
               """)

    op.execute("""insert into contract_status_history (status, changed_by, created_at, contract_id)
                  SELECT cl.status, (select name from user where id = cl.user_id), NOW(), cl.id FROM contract cl;
               """)

    op.drop_column('contract', 'description')


def schema_downgrades():
    op.add_column('contract', sa.Column('description', sa.String(length=512)))

    op.execute("""update contract as cl
                 inner join annotation_contract as ac
                 on ac.contract_id = cl.id
                set cl.description = ac.annotation""")

    op.drop_table('contract_status_history')
    op.drop_table('annotation_contract')


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
