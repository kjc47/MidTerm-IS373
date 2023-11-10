"""test migration

Revision ID: a6a949332fc9
Revises: 820dcafdaed0
Create Date: 2023-11-10 08:34:49.635723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6a949332fc9'
down_revision: Union[str, None] = '820dcafdaed0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
