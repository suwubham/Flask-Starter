import os
from sqlalchemy import create_engine, Table, MetaData


api_key = os.getenv("TEST_DATABASE_URI")
print(api_key)
