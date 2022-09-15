from sqlalchemy import  Table,Column
from sqlalchemy.sql.sqltypes import Integer,String, Date
from src.config.bd import engine, meta_data


producto = Table("producto",meta_data,
                        Column("id", Integer, primary_key=True),
                        Column("id_area_analitica", Integer, nullable=False),
                        Column("id_estado", Integer, nullable=False),
                        Column("id_formato", Integer, nullable=False),
                        Column("id_proveedor", Integer, nullable=False),
                        Column("name", String(255), nullable=False),
                        Column("lote", String(255), nullable=False),
                        Column("fecha_ingreso", Date, nullable=False),
                        Column("fecha_vencimiento", Date, nullable=False),
                        Column("cod_barra", String(255), nullable=True),
                        Column("cantidad", Integer, nullable=True)
                        )


meta_data.create_all(engine)


