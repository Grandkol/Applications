"""Initial tables

Revision ID: 6f22410f719b
Revises: 
Create Date: 2025-01-15 22:04:57.282764

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = "6f22410f719b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "application",
        sa.Column("user_name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        schema="public",
    )



def downgrade() -> None:
    op.drop_table("application", schema="public")

