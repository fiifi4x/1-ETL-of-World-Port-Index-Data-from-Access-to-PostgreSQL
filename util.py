import psycopg2
from dotenv import dotenv_values
from sqlalchemy import create_engine
dotenv_values()

def database_connect():
    config = dotenv_values('.env')
    db_name = config.get('db_name')
    db_port = config.get('db_port')
    db_host = config.get('db_host')
    db_user = config.get('db_user')
    db_password = config.get('db_password')
    engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    return engine
   