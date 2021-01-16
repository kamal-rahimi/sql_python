import pandas as pd 
import pymysql
import sqlalchemy as db
import mysql.connector
import credentials

user = credentials.user
passw = credentials.passw
host = credentials.host
port = credentials.port
schema = credentials.schema

engine_pymsql = db.create_engine(f'mysql+pymysql://{user}:{passw}@{host}:{port}/{schema}', echo=False)
enginemysqlconnector = db.create_engine(f'mysql+mysqlconnector://{user}:{passw}@{host}:{port}/{schema}', echo=False)

for engine in [engine_pymsql, enginemysqlconnector]:
    data = pd.read_sql('SELECT * FROM data_mlapp', engine)
    data.to_sql(name='sample_table3', con=engine, if_exists = 'append', index=False)

    print(data.head())

