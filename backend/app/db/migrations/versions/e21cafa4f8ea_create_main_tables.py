"""create_main_tables

Revision ID: e21cafa4f8ea
Revises: 
Create Date: 2021-11-09 12:10:11.690877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = 'e21cafa4f8ea'
down_revision = None
branch_labels = None
depends_on = None
table_name = "coveragedb"


def create_table(table_name) -> None:
    op.create_table(
        table_name,
        sa.Column("Country", sa.Text, nullable=True),
        sa.Column("Region", sa.Text, nullable=True),
        sa.Column("Code", sa.Text, nullable=True),
        sa.Column("Date", sa.Text, nullable=True),
        sa.Column("Sex", sa.Text, nullable=True),
        sa.Column("Age", sa.Text, nullable=True),
        sa.Column("AgeInt", sa.Integer, nullable=True),
        sa.Column("Metric", sa.Text, nullable=True),
        sa.Column("Measure", sa.Text, nullable=True),
        sa.Column("Value", sa.Float, nullable=True),
        sa.Column("Short", sa.Text, nullable=True),
    )

def upgrade() -> None:
    pass


def downgrade() -> None:
    pass