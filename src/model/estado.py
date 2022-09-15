from sqlalchemy import  Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy.orm import  declarative_base
from src.config.bd import engine, meta_data


estado = Table("estado",meta_data,
                        Column("id", Integer, primary_key=True),
                        Column("name", String(255), nullable=False))


meta_data.create_all(engine)