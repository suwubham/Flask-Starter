"""Add location model

Revision ID: 134ad521df1e
Revises: 
Create Date: 2024-08-21 04:36:55.143419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '134ad521df1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Country',
    sa.Column('country_id', sa.String(), nullable=False),
    sa.Column('country_name', sa.String(), nullable=False),
    sa.Column('country_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('country_id')
    )
    op.create_table('State',
    sa.Column('state_id', sa.String(), nullable=False),
    sa.Column('state_name', sa.String(), nullable=False),
    sa.Column('country_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['Country.country_id'], ),
    sa.PrimaryKeyConstraint('state_id')
    )
    op.create_table('District',
    sa.Column('district_id', sa.String(), nullable=False),
    sa.Column('district_name', sa.String(), nullable=False),
    sa.Column('state_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['State.state_id'], ),
    sa.PrimaryKeyConstraint('district_id')
    )
    op.create_table('Municipality',
    sa.Column('municipality_id', sa.String(), nullable=False),
    sa.Column('municipality_name', sa.String(), nullable=False),
    sa.Column('district_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['District.district_id'], ),
    sa.PrimaryKeyConstraint('municipality_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Municipality')
    op.drop_table('District')
    op.drop_table('State')
    op.drop_table('Country')
    # ### end Alembic commands ###
