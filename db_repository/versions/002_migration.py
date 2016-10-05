from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('fname', VARCHAR(length=128)),
    Column('lname', VARCHAR(length=128)),
    Column('nickname', VARCHAR(length=128)),
    Column('username', VARCHAR(length=128)),
    Column('password', VARCHAR(length=1024)),
    Column('email', VARCHAR(length=128)),
    Column('osis', INTEGER),
    Column('four_digit', INTEGER),
    Column('organizations', VARCHAR(length=2048)),
    Column('permissions', VARCHAR(length=1024)),
    Column('days', VARCHAR(length=128)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('fname', String(length=128)),
    Column('lname', String(length=128)),
    Column('nickname', String(length=128)),
    Column('username', String(length=128)),
    Column('password', String(length=1024)),
    Column('email', String(length=128)),
    Column('osis', Integer),
    Column('four_digit', Integer),
    Column('organizations', String(length=2048)),
    Column('wednesday', Boolean),
    Column('thursday', Boolean),
    Column('wednesday_excused', Boolean),
    Column('thursday_excused', Boolean),
    Column('wednesday_status', Integer),
    Column('thursday_status', Integer),
    Column('permissions', String(length=1024)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['days'].drop()
    post_meta.tables['user'].columns['thursday'].create()
    post_meta.tables['user'].columns['thursday_excused'].create()
    post_meta.tables['user'].columns['thursday_status'].create()
    post_meta.tables['user'].columns['wednesday'].create()
    post_meta.tables['user'].columns['wednesday_excused'].create()
    post_meta.tables['user'].columns['wednesday_status'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['days'].create()
    post_meta.tables['user'].columns['thursday'].drop()
    post_meta.tables['user'].columns['thursday_excused'].drop()
    post_meta.tables['user'].columns['thursday_status'].drop()
    post_meta.tables['user'].columns['wednesday'].drop()
    post_meta.tables['user'].columns['wednesday_excused'].drop()
    post_meta.tables['user'].columns['wednesday_status'].drop()
