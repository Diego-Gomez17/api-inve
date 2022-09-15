from sqlalchemy import  Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from src.config.bd import engine, meta_data


area_analitica = Table("area_analitica",meta_data,
                        Column("id", Integer, primary_key=True),
                        Column("name", String(255), nullable=False))

meta_data.create_all(engine)