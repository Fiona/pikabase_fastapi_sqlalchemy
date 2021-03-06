"""Add element_type table

Revision ID: ae0ff543d55f
Revises: 
Create Date: 2021-09-16 00:47:24.321756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae0ff543d55f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('element_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_element_type_id'), 'element_type', ['id'], unique=False)
    op.create_index(op.f('ix_element_type_slug'), 'element_type', ['slug'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_element_type_slug'), table_name='element_type')
    op.drop_index(op.f('ix_element_type_id'), table_name='element_type')
    op.drop_table('element_type')
    # ### end Alembic commands ###
