"""create users table

Revision ID: cdba4ceb6f3b
Revises: 
Create Date: 2023-12-16 08:38:28.502194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdba4ceb6f3b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False, comment='id'),
    sa.Column('email', sa.String(length=50), nullable=False, comment='email'),
    sa.Column('password', sa.String(length=256), nullable=False, comment='password'),
    sa.Column('name', sa.String(length=50), nullable=False, comment='name'),
    sa.Column('phone', sa.String(length=11), nullable=True, comment='phone number'),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
