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
    Column('thursday', BOOLEAN),
    Column('thursday_excused', BOOLEAN),
    Column('thursday_status', INTEGER),
    Column('wednesday', BOOLEAN),
    Column('wednesday_excused', BOOLEAN),
    Column('wednesday_status', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['email'].drop()
    pre_meta.tables['user'].columns['fname'].drop()
    pre_meta.tables['user'].columns['four_digit'].drop()
    pre_meta.tables['user'].columns['lname'].drop()
    pre_meta.tables['user'].columns['nickname'].drop()
    pre_meta.tables['user'].columns['organizations'].drop()
    pre_meta.tables['user'].columns['osis'].drop()
    pre_meta.tables['user'].columns['permissions'].drop()
    pre_meta.tables['user'].columns['thursday'].drop()
    pre_meta.tables['user'].columns['thursday_excused'].drop()
    pre_meta.tables['user'].columns['thursday_status'].drop()
    pre_meta.tables['user'].columns['wednesday'].drop()
    pre_meta.tables['user'].columns['wednesday_excused'].drop()
    pre_meta.tables['user'].columns['wednesday_status'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['email'].create()
    pre_meta.tables['user'].columns['fname'].create()
    pre_meta.tables['user'].columns['four_digit'].create()
    pre_meta.tables['user'].columns['lname'].create()
    pre_meta.tables['user'].columns['nickname'].create()
    pre_meta.tables['user'].columns['organizations'].create()
    pre_meta.tables['user'].columns['osis'].create()
    pre_meta.tables['user'].columns['permissions'].create()
    pre_meta.tables['user'].columns['thursday'].create()
    pre_meta.tables['user'].columns['thursday_excused'].create()
    pre_meta.tables['user'].columns['thursday_status'].create()
    pre_meta.tables['user'].columns['wednesday'].create()
    pre_meta.tables['user'].columns['wednesday_excused'].create()
    pre_meta.tables['user'].columns['wednesday_status'].create()
