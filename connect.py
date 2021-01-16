import pandas as pd 
import pymysql # pip install pymsql
import sqlalchemy as db # pip install sqlalchemy
import mysql.connector # requires pip install mysql-connector-python
import credentials

user = credentials.user
passw = credentials.passw
host = credentials.host
port = credentials.port
schema = credentials.schema

engine = db.create_engine(f'mysql+pymysql://{user}:{passw}@{host}:{port}/{schema}', echo=False)
engine2 = db.create_engine(f'mysql+mysqlconnector://{user}:{passw}@{host}:{port}/{schema}', echo=False)

data = pd.read_sql('SELECT * FROM data_mlapp', engine2)
data.to_sql(name='sample_table3', con=engine2, if_exists = 'append', index=False)

print(data.head())

