"""Create payments table

Revision ID: da8aabfada49
Revises: 
Create Date: 2026-08-13 10:49:39.681282

"""
from collections.abc import Sequence
from pathlib import Path

from sqlalchemy import text

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'da8aabfada49'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


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
