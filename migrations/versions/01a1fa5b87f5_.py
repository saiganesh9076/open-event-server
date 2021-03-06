"""empty message

Revision ID: 01a1fa5b87f5
Revises: 652f5bf2e030
Create Date: 2017-06-26 22:58:10.215164

"""

# revision identifiers, used by Alembic.
revision = '01a1fa5b87f5'
down_revision = '652f5bf2e030'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('is_reminder_mail_sent', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'is_reminder_mail_sent')
    ### end Alembic commands ###
