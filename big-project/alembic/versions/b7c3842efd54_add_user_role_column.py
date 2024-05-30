"""Add user role column

Revision ID: b7c3842efd54
Revises: 230ab379d748
Create Date: 2024-05-30 15:40:30.174390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7c3842efd54'
down_revision: Union[str, None] = '230ab379d748'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.Enum('SUPERADMIN', 'ADMIN', 'USER', 'GUEST', name='userrolesenum'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    # ### end Alembic commands ###