import pypyodbc
import pandas as pd

driver_name = 'SQL Server'
server_name = 'Puneet\\PUNEETSQL'
database_name = 'ML Project Datasets'

conn_str = f"""
        DRIVER= {{{driver_name}}}; 
        SERVER={server_name}; 
        Trusted_Connection=yes; 
        DATABASE={database_name};
        """
        
conn = pypyodbc.connect(conn_str)
print(conn)

df=pd.read_sql_query('Select * from walmart',conn)
print(df.head())


