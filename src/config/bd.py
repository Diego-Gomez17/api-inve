
from sqlalchemy import create_engine, MetaData
from decouple import config

DATABASE_URL=config('DATABASE_URL')
engine = create_engine(DATABASE_URL)
meta_data= MetaData()
