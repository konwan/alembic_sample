from __future__ import with_statement
import sys
sys.path.append("/Users/data/Desktop/cindy/gomi/npp/alembic/t1")
# from miku.application.group.model import Group
# from miku.application.user.model import User
# from user import User
# from role import Role
import ctest
from alembic import context
from sqlalchemy import engine_from_config, pool, MetaData
from logging.config import fileConfig
# import sys
# sys.path.append('/Users/data/Desktop/cindy/gomi/npp/miku')
# from application.group.model import Group
# from application.user.model import User

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None  # default

target_metadata = ctest.Base.metadata


def combine_metadata(*args):
    m = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(m)
    return m
# target_metadata = MetaData()
# target_metadata = combine_metadata(User.metadata)
# target_metadata = combine_metadata(Role.Base.metadata, User.Base.metadata)

'''
our_metadata = MetaData()
for metadata in (m1, m2, m3):
    for t in metadata.tables.values():
         if _your_check_here(t):
            t.tometadata(our_metadata)
'''

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
