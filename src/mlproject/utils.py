import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pypyodbc


# import pickle
import numpy as np

load_dotenv()

driver_name=os.getenv("driver_name")
server_name=os.getenv("server_name")
database_name=os.getenv('database_name')

# driver_name = 'SQL Server'
# server_name = 'Puneet\\PUNEETSQL'
# database_name = 'ML Project Datasets'

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        conn_str = f"""
        DRIVER={{{driver_name}}}; 
        SERVER={server_name}; 
        Trusted_Connection=yes; 
        DATABASE={database_name};"""
        
        conn = pypyodbc.connect(conn_str)
        # cursor = conn.cursor()
        
        logging.info("Connection Established",conn)
        df=pd.read_sql_query('Select * from walmart',conn)
        print(df.head())

        return df
    
    except Exception as ex:
        raise CustomException(ex, sys)
