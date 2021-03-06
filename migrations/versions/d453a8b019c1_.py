"""empty message

Revision ID: d453a8b019c1
Revises: 
Create Date: 2018-11-11 22:17:26.161258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd453a8b019c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Comment')
    op.drop_table('Video')
    op.drop_table('Tag')
    op.drop_table('RoomDeviceColorConnector')
    op.drop_table('Room')
    op.drop_table('AnonUser')
    op.drop_table('Views')
    op.drop_table('Geotag')
    op.drop_table('Subscription')
    op.drop_table('Likes')
    op.drop_table('Color')
    op.drop_table('Dislikes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Dislikes',
    sa.Column('User_id', sa.INTEGER(), nullable=True),
    sa.Column('Video_id', sa.VARCHAR(length=32), nullable=True),
    sa.ForeignKeyConstraint(['User_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['Video_id'], ['Video.id'], )
    )
    op.create_table('Color',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('color', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Likes',
    sa.Column('User_id', sa.INTEGER(), nullable=True),
    sa.Column('Video_id', sa.VARCHAR(length=32), nullable=True),
    sa.ForeignKeyConstraint(['User_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['Video_id'], ['Video.id'], )
    )
    op.create_table('Subscription',
    sa.Column('User_id', sa.INTEGER(), nullable=True),
    sa.Column('UserB_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['UserB_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['User_id'], ['User.id'], )
    )
    op.create_table('Geotag',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('longitude', sa.FLOAT(), nullable=False),
    sa.Column('latitude', sa.FLOAT(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('video_id', sa.VARCHAR(length=32), nullable=False),
    sa.ForeignKeyConstraint(['video_id'], ['Video.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Views',
    sa.Column('User_id', sa.INTEGER(), nullable=True),
    sa.Column('Video_id', sa.VARCHAR(length=32), nullable=True),
    sa.ForeignKeyConstraint(['User_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['Video_id'], ['Video.id'], )
    )
    op.create_table('AnonUser',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('action', sa.VARCHAR(length=64), nullable=True),
    sa.Column('time', sa.INTEGER(), nullable=True),
    sa.Column('device_width', sa.INTEGER(), nullable=True),
    sa.Column('device_height', sa.INTEGER(), nullable=True),
    sa.Column('color', sa.VARCHAR(length=64), nullable=True),
    sa.Column('top', sa.INTEGER(), nullable=True),
    sa.Column('left', sa.INTEGER(), nullable=True),
    sa.Column('res_k', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Room',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('video_id', sa.VARCHAR(length=32), nullable=True),
    sa.Column('capitan_id', sa.VARCHAR(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.ForeignKeyConstraint(['capitan_id'], ['AnonUser.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('RoomDeviceColorConnector',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('room_id', sa.INTEGER(), nullable=True),
    sa.Column('anon_id', sa.VARCHAR(), nullable=True),
    sa.Column('color_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['anon_id'], ['AnonUser.id'], ),
    sa.ForeignKeyConstraint(['color_id'], ['Color.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['Room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Tag',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=True),
    sa.Column('video_id', sa.TEXT(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['Video.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Video',
    sa.Column('id', sa.VARCHAR(length=32), nullable=False),
    sa.Column('title', sa.VARCHAR(length=140), nullable=False),
    sa.Column('path', sa.VARCHAR(length=256), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('user_login', sa.VARCHAR(), nullable=True),
    sa.Column('longitude', sa.FLOAT(), nullable=True),
    sa.Column('latitude', sa.FLOAT(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Comment',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=True),
    sa.Column('video_id', sa.TEXT(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['Video.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
