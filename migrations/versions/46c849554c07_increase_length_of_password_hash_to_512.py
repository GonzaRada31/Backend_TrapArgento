"""Increase length of password_hash to 512

Revision ID: 46c849554c07
Revises: 80a88b09045c
Create Date: 2024-07-02 19:06:41.956221

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46c849554c07'
down_revision = '80a88b09045c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artista', schema=None) as batch_op:
        batch_op.alter_column('nombre',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=100),
               existing_nullable=True)

    with op.batch_alter_table('cancion', schema=None) as batch_op:
        batch_op.alter_column('titulo',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('album',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=100),
               existing_nullable=True)

    with op.batch_alter_table('disco', schema=None) as batch_op:
        batch_op.alter_column('titulo',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=100),
               existing_nullable=True)

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('nombre',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('apellido',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=True)

    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.alter_column('titulo',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.alter_column('titulo',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)
        batch_op.alter_column('apellido',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=64),
               existing_nullable=True)
        batch_op.alter_column('nombre',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=64),
               existing_nullable=True)

    with op.batch_alter_table('disco', schema=None) as batch_op:
        batch_op.alter_column('titulo',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)

    with op.batch_alter_table('cancion', schema=None) as batch_op:
        batch_op.alter_column('album',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)
        batch_op.alter_column('titulo',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)

    with op.batch_alter_table('artista', schema=None) as batch_op:
        batch_op.alter_column('nombre',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=64),
               existing_nullable=True)

    # ### end Alembic commands ###
