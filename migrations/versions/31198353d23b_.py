"""empty message

Revision ID: 31198353d23b
Revises: de0c068c2560
Create Date: 2019-05-24 11:05:23.037974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31198353d23b'
down_revision = 'de0c068c2560'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'whfrj_products', 'whfrj_classification', ['cid'], ['cid'])
    op.add_column('whfrj_users', sa.Column('add_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('whfrj_users', 'add_time')
    op.drop_constraint(None, 'whfrj_products', type_='foreignkey')
    # ### end Alembic commands ###