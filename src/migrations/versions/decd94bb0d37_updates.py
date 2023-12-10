"""updates

Revision ID: decd94bb0d37
Revises: 33125c9eb94f
Create Date: 2023-12-10 23:59:48.184984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'decd94bb0d37'
down_revision = '33125c9eb94f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'calling_to_emergency', ['id'])
    op.create_unique_constraint(None, 'log', ['id'])
    op.add_column('sensor', sa.Column('active', sa.Boolean(), nullable=False))
    op.alter_column('sensor', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.create_unique_constraint(None, 'sensor', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sensor', type_='unique')
    op.alter_column('sensor', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_column('sensor', 'active')
    op.drop_constraint(None, 'log', type_='unique')
    op.drop_constraint(None, 'calling_to_emergency', type_='unique')
    # ### end Alembic commands ###