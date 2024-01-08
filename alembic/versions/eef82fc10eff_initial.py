"""initial

Revision ID: eef82fc10eff
Revises: 4b7ee71c48ff
Create Date: 2024-01-06 23:01:19.304518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eef82fc10eff'
down_revision: Union[str, None] = '4b7ee71c48ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('propostas_contraparte',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('id_contraparte', sa.Integer(), nullable=True),
    sa.Column('data_aprovacao_limite', sa.DateTime(), nullable=True),
    sa.Column('grupo', sa.String(), nullable=True),
    sa.Column('tipo_limite', sa.Integer(), nullable=True),
    sa.Column('data_proposta', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('tipo_analise', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('valor_utilizado_conversao', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['clientes.id'], ),
    sa.ForeignKeyConstraint(['id_contraparte'], ['tipos_rating_cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_propostas_contraparte_id'), 'propostas_contraparte', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_propostas_contraparte_id'), table_name='propostas_contraparte')
    op.drop_table('propostas_contraparte')
    # ### end Alembic commands ###