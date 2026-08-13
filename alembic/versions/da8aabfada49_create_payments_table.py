"""Create payments table

Revision ID: da8aabfada49
Revises: 
Create Date: 2026-08-13 10:49:39.681282

"""
from typing import Sequence, Union
from sqlalchemy import text
from pathlib import Path
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da8aabfada49'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    sql_path = Path(__file__).parent.parent / "sql" / "create_payments_table.sql"
    with sql_path.open() as f:
        sql = f.read()
        op.execute(text(sql))


def downgrade() -> None:
    """Downgrade schema."""
    sql_path = Path(__file__).parent.parent / "sql" / "drop_payments_table.sql"
    with sql_path.open() as f:
        sql = f.read()
        op.execute(text(sql))
