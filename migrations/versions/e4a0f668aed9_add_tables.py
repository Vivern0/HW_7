"""Add tables

Revision ID: e4a0f668aed9
Revises: 5590100f2613
Create Date: 2024-03-07 20:11:26.842168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4a0f668aed9'
down_revision: Union[str, None] = '5590100f2613'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lecturers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('group_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_fk'], ['groups.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subject_name', sa.String(length=100), nullable=False),
    sa.Column('lecturer_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lecturer_fk'], ['lecturers.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.Column('date', sa.DATE(), nullable=False),
    sa.Column('student_fk', sa.Integer(), nullable=False),
    sa.Column('subject_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_fk'], ['students.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_fk'], ['subjects.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('marks')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('lecturers')
    op.drop_table('groups')
