# create a mysql database connection from sqlalchemy to an endpoint in the database

from sqlalchemy import create_engine,MetaData


engine = create_engine("mysql+pymysql://root:Imbrgv1234$$@localhost:3306/py_crud")
meta = MetaData()
con = engine.connect()
