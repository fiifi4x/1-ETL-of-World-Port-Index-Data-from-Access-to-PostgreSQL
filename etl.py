import pyodbc
import psycopg2
import pandas as pd
from util import database_connect

def conn_str():
    access_driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    file_path = r"C:\Users\Grony 4\Desktop\2A) Cap 3 (Access)\WPI.mdb"
    conn = "DRIVER={};DBQ={};".format(access_driver, file_path)           
    py_connect = pyodbc.connect(conn)  # database connection with pyodbc
    return py_connect

access_engine = conn_str()
postgres_engine = database_connect()

def el_country_codes():
    # extract country_codes table from MICROSOFT ACCESS 
    query = 'select * from [Country Codes]'
    country_codes = pd.read_sql(query, access_engine)
    print('Country codes table extracted from MS Access Database successfully')
    # load extracted country codes table into postgres database 
    table_name = 'country_codes'
    country_codes.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('Country codes table loaded into Postgres Database successfully')

def el_country_codes_old():
    # extract country codes old table from MICROSOFT ACCESS 
    query = 'select * from CountryCodesOld'
    country_codes_old = pd.read_sql(query, access_engine)
    print('country_codes_old table extracted from MS Access Database successfully')
    # load extracted country codes old table into postgres database 
    table_name = 'country_codes_old'
    country_codes_old.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('Country Codes Old table loaded into Postgres Database successfully')

def el_depth_code_lut():
    # extract depth_code_lut table from MICROSOFT ACCESS 
    query = 'select * from [Depth Code LUT]'
    depth_code_lut = pd.read_sql(query, access_engine)
    print('depth_code_lut table extracted from MS Access Database successfully')
    # load extracted depth_code_lut table into postgres database 
    table_name = 'depth_code_lut'
    depth_code_lut.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('depth_code_lut table loaded into Postgres Database successfully')

def el_drydock_marine_railway():
    # extract drydock_marine_railway table from MICROSOFT ACCESS 
    query = 'select * from [Drydock_Marine Railway]'
    drydock_marine_railway = pd.read_sql(query, access_engine)
    print('drydock_marine_railway table extracted from MS Access Database successfully')
    # load extracted drydock_marine_railway table into postgres database 
    table_name = 'drydock_marine_railway'
    drydock_marine_railway.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('drydock_marine_railway table loaded into Postgres Database successfully')

def el_harbor_size():
    # extract country_codes table from MICROSOFT ACCESS 
    query = 'select * from [Harbor Size LUT]'
    harbor_size = pd.read_sql(query, access_engine)
    print('harbor_size table extracted from MS Access Database successfully')
    # load extracted harbor_size table into postgres database 
    table_name = 'harbor_size'
    harbor_size.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('harbor_size table loaded into Postgres Database successfully')

def el_harbor_type():
    # extract country_codes table from MICROSOFT ACCESS 
    query = 'select * from [Harbor Type]'
    harbor_type = pd.read_sql(query, access_engine)
    print('harbor_type table extracted from MS Access Database successfully')
    # load extracted harbor_type table into postgres database 
    table_name = 'harbor_type'
    harbor_type.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('harbor_type table loaded into Postgres Database successfully')

def el_maximum_size_vessel():
    # extract maximum_size_vessel table from MICROSOFT ACCESS 
    query = 'select * from [maximum_size_vessel]'
    maximum_size_vessel = pd.read_sql(query, access_engine)
    print('maximum_size_vessel table extracted from MS Access Database successfully')
    # load extracted maximum_size_vessel table into postgres database 
    table_name = 'maximum_size_vessel'
    maximum_size_vessel.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('maximum_size_vessel table loaded into Postgres Database successfully')

def el_repairs_code():
    # extract repairs_code table from MICROSOFT ACCESS 
    query = 'select * from [repairs_code]'
    repairs_code = pd.read_sql(query, access_engine)
    print('repairs_code table extracted from MS Access Database successfully')
    # load extracted repairs_code table into postgres database 
    table_name = 'repairs_code'
    repairs_code.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('repairs_code table loaded into Postgres Database successfully')

def el_shelter_afforded():
    # extract shelter_afforded table from MICROSOFT ACCESS 
    query = 'select * from shelter_afforded'
    shelter_afforded = pd.read_sql(query, access_engine)
    print('shelter_afforded table extracted from MS Access Database successfully')
    # load extracted shelter_afforded table into postgres database 
    table_name = 'shelter_afforded'
    shelter_afforded.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('shelter_afforded table loaded into Postgres Database successfully')

def el_new_all():
    # extract new_all table from MICROSOFT ACCESS 
    query = 'select * from new_all'
    new_all = pd.read_sql(query, access_engine)
    print('new_all table extracted from MS Access Database successfully')
    # load extracted new_all table into postgres database 
    table_name = 'new_all'
    new_all.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('new_all table loaded into Postgres Database successfully')

def el_wpi_import():
    # extract wpi_import table from MICROSOFT ACCESS 
    query = 'select * from wpi_import'
    wpi_import = pd.read_sql(query, access_engine)
    print('wpi_import table extracted from MS Access Database successfully')
    # load extracted wpi_import table into postgres database 
    table_name = 'wpi_import'
    wpi_import.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('wpi_import table loaded into Postgres Database successfully')

def el_wpi_region():
    # extract wpi_region table from MICROSOFT ACCESS 
    query = 'select * from wpi_region'
    wpi_region = pd.read_sql(query, access_engine)
    print('wpi_region table extracted from MS Access Database successfully')
    # load extracted wpi_region table into postgres database 
    table_name = 'wpi_region'
    wpi_region.to_sql(table_name, postgres_engine, if_exists='replace', index=False)
    print('wpi_region table loaded into Postgres Database successfully')

  