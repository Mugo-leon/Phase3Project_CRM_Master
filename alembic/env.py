from logging.config import fileConfig
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool

from alembic import context

# Import your model classes for autogenerate support
from models.models import Base

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging. This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add this line to configure the target_metadata
target_metadata = Base.metadata

# Define the engine here
engine = create_engine(config.get_main_option("sqlalchemy.url"))

# other import and configuration...

def run_migrations_online():
    # other configurations...

    with context.begin_transaction():
        context.run_migrations()

# When run as a script, we want to run against a particular database.
# This configures the context with just that information.
if context.is_offline_mode():
    run_migrations_online()
else:
    # The first and second arguments here are the Alembic command-line arguments.
    # To run this script from the current directory, use
    # $ alembic -c ./path/to/alembic.ini script revision --autogenerate -m "your message"
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        run_migrations_online()
