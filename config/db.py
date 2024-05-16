from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:170815Janis.@localhost:3306/storedb3")

meta = MetaData()

conn = engine.connect()